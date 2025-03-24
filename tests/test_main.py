import pytest
import json
import os
from src.main import load_transactions, display_transactions

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
        }
    ]

@pytest.fixture
def transactions_file(tmp_path, sample_transactions):
    file_path = tmp_path / "transactions.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(sample_transactions, f, ensure_ascii=False, indent=2)
    return str(file_path)

def test_load_transactions(transactions_file):
    transactions = load_transactions(transactions_file)
    assert len(transactions) == 2
    assert transactions[0]['description'] == 'Покупка продуктов в магазине'
    assert transactions[1]['description'] == 'Оплата услуг ЖКХ'

def test_load_transactions_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_transactions('nonexistent_file.json')

def test_load_transactions_invalid_json(tmp_path):
    invalid_file = tmp_path / "invalid.json"
    with open(invalid_file, 'w', encoding='utf-8') as f:
        f.write('invalid json content')
    
    with pytest.raises(json.JSONDecodeError):
        load_transactions(str(invalid_file))

def test_display_transactions(capsys, sample_transactions):
    display_transactions(sample_transactions)
    captured = capsys.readouterr()
    
    # Проверяем, что вывод содержит все необходимые поля
    assert "Дата:" in captured.out
    assert "Описание:" in captured.out
    assert "Сумма:" in captured.out
    assert "Статус:" in captured.out
    
    # Проверяем, что вывод содержит данные из транзакций
    assert "Покупка продуктов в магазине" in captured.out
    assert "1500.50" in captured.out
    assert "RUB" in captured.out
    assert "COMPLETED" in captured.out

def test_display_transactions_empty(capsys):
    display_transactions([])
    captured = capsys.readouterr()
    assert "Транзакции не найдены." in captured.out

def test_display_transactions_missing_fields(capsys):
    transactions = [
        {
            'date': '2024-03-20T10:00:00Z',
            'description': 'Тестовая транзакция'
        }
    ]
    display_transactions(transactions)
    captured = capsys.readouterr()
    
    # Проверяем, что отсутствующие поля отображаются как "Н/Д"
    assert "Дата: 2024-03-20T10:00:00Z" in captured.out
    assert "Описание: Тестовая транзакция" in captured.out
    assert "Сумма: Н/Д Н/Д" in captured.out
    assert "Статус: Н/Д" in captured.out 