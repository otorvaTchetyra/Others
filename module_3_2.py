def send_email(message, recipient, sender):
    if recipient != '@' and not any((recipient.endswith('.com'), recipient.endswith('.ru'), recipient.endswith('.net'))):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе")
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')  
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', 'university.help@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.com', 'university.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.uk', 'urban.teacher@mail.ru') 
# I swaped 'urban.student@mail.ru (.uk)' und 'urban.teacher.uk (.ru)' to call this condition "Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')




# def send_email(message, recipient, sender):
#     sender = "university.help@gmail.com"
#     if message and recipient != "@" or recipient.endswith != ".com" / ".ru" / ".net": #why do we need to use this arg message?
#        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}') #what's wrong with them?
#     elif recipient == sender:
#         print("Нельзя отправить письмо самому себе")
#     elif sender != 'university.help@gmail.com':
#         print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.') 
#     else:
#         print(f'Письмо упешно отправдено с адреса {sender} на адрес{recipient}')

# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com','university.help@gmail.com') #can we avoid several calls of the fun?
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.com', 'university.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')

