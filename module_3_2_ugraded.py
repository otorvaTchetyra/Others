def send_email(message, recipient, sender="university.help@gmail.com"):
    answer = "Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient + " - " + message
    if "@" not in recipient or "@" not in sender:
        answer = "Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient + " " + message
    elif sender[len(sender)-4:] != ".com" and sender[len(sender)-3:] != ".ru" and sender[len(sender)-4:] != ".net":
        answer = "Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient + " - " + message
    elif recipient[len(recipient)-4:] != ".com" and recipient[len(recipient)-3:] != ".ru" and recipient[len(recipient)-4:] != ".net":
        answer = "Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient + " - " + message
    elif sender==recipient:
        answer = "Нельзя отправить письмо самому себе!" + " - " + message
    elif sender!="university.help@gmail.com":
        answer = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient + " - " + message
    return(answer)

print(send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com"))
print(send_email("Вы видите это сообщение как лучший студент курса", "urban.fan@mail.ru", sender="urban.info@gmail.com"))
print(send_email("Пожалуйста, исправьте задание", "urban.student@mail.ru", sender="urban.teacher@mail.uk"))
print(send_email("Напоминаю самому себе о вебинаре", "urban.teacher@mail.ru", sender="urban.teacher@mail.ru"))