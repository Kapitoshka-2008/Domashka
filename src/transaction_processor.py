import re
from typing import List, Dict, Any
from datetime import datetime
from .logger import setup_logger

logger = setup_logger(__name__)

def filter_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по описанию с использованием регулярных выражений.
    
    Args:
        transactions: Список транзакций
        search_string: Строка для поиска в описании
        
    Returns:
        Отфильтрованный список транзакций
    """
    try:
        logger.info(f"Начало фильтрации транзакций по описанию: {search_string}")
        pattern = re.compile(search_string, re.IGNORECASE)
        filtered_transactions = [
            transaction for transaction in transactions
            if pattern.search(transaction.get('description', ''))
        ]
        logger.info(f"Найдено {len(filtered_transactions)} транзакций, соответствующих поиску")
        return filtered_transactions
    except Exception as e:
        logger.error(f"Ошибка при фильтрации транзакций: {str(e)}")
        raise

def count_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по категориям.
    
    Args:
        transactions: Список транзакций
        categories: Список категорий для подсчета
        
    Returns:
        Словарь с количеством транзакций по каждой категории
    """
    try:
        logger.info(f"Начало подсчета транзакций по категориям: {categories}")
        result = {category: 0 for category in categories}
        
        for transaction in transactions:
            description = transaction.get('description', '').lower()
            for category in categories:
                if category.lower() in description:
                    result[category] += 1
                    break
        
        logger.info(f"Подсчет завершен: {result}")
        return result
    except Exception as e:
        logger.error(f"Ошибка при подсчете транзакций по категориям: {str(e)}")
        raise

def filter_by_status(transactions: List[Dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по статусу.
    
    Args:
        transactions: Список транзакций
        status: Статус для фильтрации
        
    Returns:
        Отфильтрованный список транзакций
    """
    try:
        logger.info(f"Начало фильтрации транзакций по статусу: {status}")
        filtered_transactions = [
            transaction for transaction in transactions
            if transaction.get('status', '').upper() == status.upper()
        ]
        logger.info(f"Найдено {len(filtered_transactions)} транзакций со статусом {status}")
        return filtered_transactions
    except Exception as e:
        logger.error(f"Ошибка при фильтрации транзакций по статусу: {str(e)}")
        raise

def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Сортирует транзакции по дате.
    
    Args:
        transactions: Список транзакций
        reverse: True для сортировки по убыванию, False по возрастанию
        
    Returns:
        Отсортированный список транзакций
    """
    try:
        logger.info(f"Начало сортировки транзакций по дате (reverse={reverse})")
        sorted_transactions = sorted(
            transactions,
            key=lambda x: datetime.strptime(x.get('date', ''), '%Y-%m-%dT%H:%M:%SZ'),
            reverse=reverse
        )
        logger.info("Сортировка завершена")
        return sorted_transactions
    except Exception as e:
        logger.error(f"Ошибка при сортировке транзакций: {str(e)}")
        raise

def filter_by_currency(transactions: List[Dict[str, Any]], currency: str = 'RUB') -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по валюте.
    
    Args:
        transactions: Список транзакций
        currency: Код валюты для фильтрации
        
    Returns:
        Отфильтрованный список транзакций
    """
    try:
        logger.info(f"Начало фильтрации транзакций по валюте: {currency}")
        filtered_transactions = [
            transaction for transaction in transactions
            if transaction.get('currency', '').upper() == currency.upper()
        ]
        logger.info(f"Найдено {len(filtered_transactions)} транзакций в валюте {currency}")
        return filtered_transactions
    except Exception as e:
        logger.error(f"Ошибка при фильтрации транзакций по валюте: {str(e)}")
        raise 