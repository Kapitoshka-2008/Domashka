# account_number = input()
# # принимает номер аккаунта пользователя
# card_number = input()
# # принимает номер карточки

from typing import List
from .logger import setup_logger

logger = setup_logger('masks')


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя видимыми только последние 4 цифры.
    
    Args:
        card_number: Номер карты
        
    Returns:
        str: Замаскированный номер карты
    """
    try:
        if not card_number or len(card_number) < 4:
            logger.warning(f"Некорректный номер карты: {card_number}")
            return card_number
            
        masked = '*' * (len(card_number) - 4) + card_number[-4:]
        logger.info(f"Номер карты {card_number} успешно замаскирован")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировании номера карты {card_number}: {str(e)}")
        return card_number


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя видимыми только последние 4 цифры.
    
    Args:
        account_number: Номер счета
        
    Returns:
        str: Замаскированный номер счета
    """
    try:
        if not account_number or len(account_number) < 4:
            logger.warning(f"Некорректный номер счета: {account_number}")
            return account_number
            
        masked = '*' * (len(account_number) - 4) + account_number[-4:]
        logger.info(f"Номер счета {account_number} успешно замаскирован")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировании номера счета {account_number}: {str(e)}")
        return account_number


# выводим результат
# print(mask_card_number(card_number))
# print(mask_account_number(account_number))
