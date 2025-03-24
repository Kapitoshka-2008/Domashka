import pytest
from datetime import datetime
from src.transaction_processor import (
    filter_by_description,
    count_by_category,
    filter_by_status,
    sort_by_date,
    filter_by_currency
)

@pytest.fixture
def sample_transactions():
    return [
        {
            'date': '2024-03-20T10:00:00Z',
            'description': 'Покупка продуктов в магазине',
            'amount': 1500.50,
            'currency': 'RUB',
            'status': 'COMPLETED'
        },
        {
            'date': '2024-03-19T15:30:00Z',
            'description': 'Оплата услуг ЖКХ',
            'amount': 3000.00,
            'currency': 'RUB',
            'status': 'PENDING'
        },
        {
            'date': '2024-03-18T09:15:00Z',
            'description': 'Перевод в USD',
            'amount': 100.00,
            'currency': 'USD',
            'status': 'COMPLETED'
        }
    ]

def test_filter_by_description(sample_transactions):
    # Тест поиска по точному совпадению
    result = filter_by_description(sample_transactions, r'продуктов')
    assert len(result) == 1
    assert result[0]['description'] == 'Покупка продуктов в магазине'
    
    # Тест поиска с использованием регулярного выражения
    result = filter_by_description(sample_transactions, r'^Оплата')
    assert len(result) == 1
    assert result[0]['description'] == 'Оплата услуг ЖКХ'
    
    # Тест поиска с учетом регистра
    result = filter_by_description(sample_transactions, r'USD')
    assert len(result) == 1
    assert result[0]['currency'] == 'USD'

def test_count_by_category(sample_transactions):
    categories = ['продукты', 'услуги', 'перевод']
    result = count_by_category(sample_transactions, categories)
    
    assert result['продукты'] == 1
    assert result['услуги'] == 1
    assert result['перевод'] == 1
    
    # Тест с категорией, которой нет в транзакциях
    categories = ['продукты', 'развлечения']
    result = count_by_category(sample_transactions, categories)
    assert result['развлечения'] == 0

def test_filter_by_status(sample_transactions):
    # Тест фильтрации по статусу COMPLETED
    result = filter_by_status(sample_transactions, 'COMPLETED')
    assert len(result) == 2
    assert all(t['status'] == 'COMPLETED' for t in result)
    
    # Тест фильтрации по статусу PENDING
    result = filter_by_status(sample_transactions, 'PENDING')
    assert len(result) == 1
    assert result[0]['status'] == 'PENDING'
    
    # Тест фильтрации по несуществующему статусу
    result = filter_by_status(sample_transactions, 'CANCELLED')
    assert len(result) == 0

def test_sort_by_date(sample_transactions):
    # Тест сортировки по возрастанию
    result = sort_by_date(sample_transactions, reverse=False)
    assert result[0]['date'] == '2024-03-18T09:15:00Z'
    assert result[-1]['date'] == '2024-03-20T10:00:00Z'
    
    # Тест сортировки по убыванию
    result = sort_by_date(sample_transactions, reverse=True)
    assert result[0]['date'] == '2024-03-20T10:00:00Z'
    assert result[-1]['date'] == '2024-03-18T09:15:00Z'

def test_filter_by_currency(sample_transactions):
    # Тест фильтрации по RUB
    result = filter_by_currency(sample_transactions, 'RUB')
    assert len(result) == 2
    assert all(t['currency'] == 'RUB' for t in result)
    
    # Тест фильтрации по USD
    result = filter_by_currency(sample_transactions, 'USD')
    assert len(result) == 1
    assert result[0]['currency'] == 'USD'
    
    # Тест фильтрации по несуществующей валюте
    result = filter_by_currency(sample_transactions, 'EUR')
    assert len(result) == 0
    
    # Тест с пустым значением валюты (должен использовать RUB по умолчанию)
    result = filter_by_currency(sample_transactions, '')
    assert len(result) == 2
    assert all(t['currency'] == 'RUB' for t in result) 