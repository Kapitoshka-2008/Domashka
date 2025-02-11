# src/widget.py
from typing import Any

from masks import mask_account_number, mask_card_number


def mask_account_card(account_info: str) -> str:
    """
    Функция для маскировки номеров карт и счетов.

    :param account_info: Строка с типом и номером карты или счета.
    :return: Строка с замаскированным номером.
    """
    if (
        "Visa" in account_info
        or "Maestro" in account_info
        or "MasterCard" in account_info
    ):
        return mask_card_number(account_info)
    elif "Счет" in account_info:
        return mask_account_number(account_info)
    else:
        raise ValueError("Неизвестный тип карты или счета.")


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO 8601 в формат ДД.ММ.ГГГГ.

    :param date_str: Дата в формате ISO 8601.
    :return: Дата в формате ДД.ММ.ГГГГ.
    """
    try:
        from datetime import datetime

        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError as e:
        print(f"Ошибка при преобразовании даты: {e}")
        return ""
