import json
import pytest
from pathlib import Path
from src.utils import load_transactions


def test_load_transactions_valid_file(tmp_path):
    # Создаем тестовый JSON файл
    test_data = [
        {"amount": 100, "currency": "RUB"},
        {"amount": 200, "currency": "USD"}
    ]
    file_path = tmp_path / "test_transactions.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f)
    
    # Проверяем загрузку
    result = load_transactions(str(file_path))
    assert result == test_data


def test_load_transactions_empty_file(tmp_path):
    # Создаем пустой файл
    file_path = tmp_path / "empty.json"
    file_path.touch()
    
    # Проверяем загрузку
    result = load_transactions(str(file_path))
    assert result == []


def test_load_transactions_invalid_json(tmp_path):
    # Создаем файл с невалидным JSON
    file_path = tmp_path / "invalid.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("invalid json")
    
    # Проверяем загрузку
    result = load_transactions(str(file_path))
    assert result == []


def test_load_transactions_nonexistent_file():
    # Проверяем загрузку несуществующего файла
    result = load_transactions("nonexistent.json")
    assert result == []


def test_load_transactions_not_list(tmp_path):
    # Создаем файл с JSON, но не списком
    test_data = {"amount": 100, "currency": "RUB"}
    file_path = tmp_path / "not_list.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f)
    
    # Проверяем загрузку
    result = load_transactions(str(file_path))
    assert result == [] 