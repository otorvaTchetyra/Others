import re

def validate_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return email
    else:
        raise ValueError(f"Некорректный формат электронного адреса '{email}'")

def send_email(message, recipient, sender="university.help@gmail.com"):
    validated_recipient = validate_email(recipient)
    validated_sender = validate_email(sender)
    if validated_recipient == validated_sender:
        print("Нельзя отправить письмо самому себе")
    else:
        print(f'Письмо успешно отправлено с адреса {validated_sender} на адрес {validated_recipient}')

try:
    send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com")
    send_email("Вы видите это сообщение как лучший студент курса", "urban.fan@mail.ru", sender="urban.info@gmail.com")
    send_email("Пожалуйста, исправьте задание", "urban.student@mail.ru", sender="urban.teacher@mail.uk")
    send_email("Напоминаю самому себе о вебинаре", "urban.teacher@mail.ru", sender="urban.teacher@mail.ru")
except ValueError as e:
    print(e)