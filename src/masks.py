account_number = input()
# принимает номер аккаунта пользователя
card_number = input()
# принимает номер карточки


def mask_card_number(card_number: str) -> str:
    """
    функция обрабатывает в нужный нам формат для вывода: XXXX XX** **** XXXX ,
    где X — это цифра номера
    :param card_number:
    :return:
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def mask_account_number(account_number: str) -> str:
    """функция обрабатывает в нужный нам формат для вывода: **XXXX , где X — это цифра номера.

    :param account_number:
    :return:
    """
    return f"** {account_number[-4:]}"


# выводим результат
print(mask_card_number(card_number))
print(mask_account_number(account_number))
