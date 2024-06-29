def send_email(message, recipient, *, sender='univercity.help@gmail.com'):
    # Проверка на отправку самому себе
    if sender == recipient:
        return print("Нельзя отправить письмо самому себе!")

    # Разворот E-mail для последующего определения окончания E-mail внутри цикла
    mail_end_check_r = recipient[::-1]
    mail_end_check_s = sender[::-1]

    # Список из окончаний E-mail
    end_list = ['.com', '.ru', '.net']

    # Проверка на наличие знака "@", если не найдёт, то функция завершится
    if '@' not in recipient or '@' not in sender:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    # Определение флагов для проверки окончания почты отправителя и получателя на наличие окончания из списка "end_list"
    is_have_end_r = False
    is_have_end_s = False

    # Проверка окончания почты отправителя и получателя на наличие окончания из списка "end_list"
    for end in end_list:
        if end[::-1] in mail_end_check_s[:4]:  # Окончание определяется здесь
            is_have_end_s = True
        if end[::-1] in mail_end_check_r[:4]:  # Окончание определяется здесь
            is_have_end_r = True
        if is_have_end_r and is_have_end_s:  # Проверка на досрочное нахождение нужных окончаний
            break

    # Если хоть у одной почты не найдётся нужного окончания, то функция завершится так
    if not is_have_end_r or not is_have_end_s:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    # Проверка на нестандартного отправителя
    if sender != 'univercity.help@gmail.com':
        return print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

    # Если все проверки пройдены
    return print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
