import json
from typing import List, Dict, Any
from .transaction_processor import (
    filter_by_description,
    count_by_category,
    filter_by_status,
    sort_by_date,
    filter_by_currency
)
from .logger import setup_logger

logger = setup_logger(__name__)

def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает транзакции из JSON файла.
    
    Args:
        file_path: Путь к файлу с транзакциями
        
    Returns:
        Список транзакций
    """
    try:
        logger.info(f"Загрузка транзакций из файла: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
        logger.info(f"Загружено {len(transactions)} транзакций")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при загрузке транзакций: {str(e)}")
        raise

def display_transactions(transactions: List[Dict[str, Any]]) -> None:
    """
    Выводит транзакции в консоль.
    
    Args:
        transactions: Список транзакций для вывода
    """
    if not transactions:
        print("\nТранзакции не найдены.")
        return
    
    print("\nСписок транзакций:")
    print("-" * 80)
    for transaction in transactions:
        print(f"Дата: {transaction.get('date', 'Н/Д')}")
        print(f"Описание: {transaction.get('description', 'Н/Д')}")
        print(f"Сумма: {transaction.get('amount', 'Н/Д')} {transaction.get('currency', 'RUB')}")
        print(f"Статус: {transaction.get('status', 'Н/Д')}")
        print("-" * 80)

def display_menu() -> None:
    """Выводит меню программы."""
    print("\nМеню:")
    print("1. Фильтр по описанию (регулярное выражение)")
    print("2. Подсчет по категориям")
    print("3. Фильтр по статусу")
    print("4. Сортировка по дате")
    print("5. Фильтр по валюте")
    print("6. Показать все транзакции")
    print("0. Выход")

def get_status_choice() -> str:
    """
    Получает выбор статуса от пользователя.
    
    Returns:
        Выбранный статус
    """
    valid_statuses = ['COMPLETED', 'PENDING', 'CANCELLED']
    while True:
        print("\nДоступные статусы:")
        for i, status in enumerate(valid_statuses, 1):
            print(f"{i}. {status}")
        
        try:
            choice = int(input("\nВыберите номер статуса: "))
            if 1 <= choice <= len(valid_statuses):
                return valid_statuses[choice - 1]
            print("Неверный номер статуса. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число.")

def ask_for_additional_filtering(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Спрашивает пользователя о дополнительной фильтрации.
    
    Args:
        transactions: Список транзакций для фильтрации
        
    Returns:
        Отфильтрованный список транзакций
    """
    while True:
        print("\nХотите применить дополнительную фильтрацию?")
        print("1. Фильтр по валюте")
        print("2. Сортировка по дате")
        print("3. Нет, показать результаты")
        
        choice = input("\nВыберите действие (1-3): ")
        
        if choice == '1':
            currency = input("\nВведите код валюты (по умолчанию RUB): ").strip().upper() or 'RUB'
            transactions = filter_by_currency(transactions, currency)
        elif choice == '2':
            reverse = input("\nСортировать по убыванию? (да/нет): ").lower() == 'да'
            transactions = sort_by_date(transactions, reverse)
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
    
    return transactions

def main() -> None:
    """Основная функция программы."""
    try:
        print("\nДобро пожаловать в программу обработки финансовых транзакций!")
        print("=" * 50)
        
        # Загрузка транзакций
        transactions = load_transactions('data/transactions.json')
        
        while True:
            display_menu()
            choice = input("\nВыберите действие (0-6): ")
            
            if choice == '0':
                print("\nСпасибо за использование программы!")
                break
                
            elif choice == '1':
                search_string = input("\nВведите регулярное выражение для поиска: ")
                filtered = filter_by_description(transactions, search_string)
                filtered = ask_for_additional_filtering(filtered)
                display_transactions(filtered)
                
            elif choice == '2':
                categories = input("\nВведите категории через запятую: ").split(',')
                categories = [cat.strip() for cat in categories]
                result = count_by_category(transactions, categories)
                print("\nКоличество транзакций по категориям:")
                for category, count in result.items():
                    print(f"{category}: {count}")
                
                # Спрашиваем, хочет ли пользователь увидеть детали
                if input("\nХотите увидеть детали транзакций? (да/нет): ").lower() == 'да':
                    filtered = []
                    for category in categories:
                        filtered.extend(filter_by_description(transactions, category.lower()))
                    filtered = ask_for_additional_filtering(filtered)
                    display_transactions(filtered)
                    
            elif choice == '3':
                status = get_status_choice()
                filtered = filter_by_status(transactions, status)
                filtered = ask_for_additional_filtering(filtered)
                display_transactions(filtered)
                
            elif choice == '4':
                reverse = input("\nСортировать по убыванию? (да/нет): ").lower() == 'да'
                sorted_transactions = sort_by_date(transactions, reverse)
                sorted_transactions = ask_for_additional_filtering(sorted_transactions)
                display_transactions(sorted_transactions)
                
            elif choice == '5':
                currency = input("\nВведите код валюты (по умолчанию RUB): ").strip().upper() or 'RUB'
                filtered = filter_by_currency(transactions, currency)
                filtered = ask_for_additional_filtering(filtered)
                display_transactions(filtered)
                
            elif choice == '6':
                filtered = ask_for_additional_filtering(transactions)
                display_transactions(filtered)
                
            else:
                print("\nНеверный выбор. Попробуйте снова.")
                
    except Exception as e:
        logger.error(f"Ошибка в главном цикле программы: {str(e)}")
        print(f"\nПроизошла ошибка: {str(e)}")

if __name__ == '__main__':
    main() 