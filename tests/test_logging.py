import pytest
import logging
import os
from pathlib import Path
from src.utils import load_transactions
from src.masks import mask_card_number, mask_account_number


def test_logging_setup():
    # Проверяем, что директория logs создана
    assert Path("logs").exists()
    
    # Проверяем, что файлы логов созданы
    assert Path("logs/utils.log").exists()
    assert Path("logs/masks.log").exists()


def test_utils_logging(tmp_path):
    # Создаем тестовый JSON файл
    test_data = [
        {"amount": 100, "currency": "RUB"},
        {"amount": 200, "currency": "USD"}
    ]
    file_path = tmp_path / "test_transactions.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("invalid json")
    
    # Проверяем логирование ошибки
    result = load_transactions(str(file_path))
    assert result == []
    
    # Проверяем содержимое лог-файла
    with open("logs/utils.log", 'r', encoding='utf-8') as f:
        log_content = f.read()
        assert "ERROR" in log_content
        assert "Ошибка при разборе JSON файла" in log_content


def test_masks_logging():
    # Проверяем логирование успешного маскирования
    card_number = "1234567890123456"
    masked_card = mask_card_number(card_number)
    assert masked_card == "************3456"
    
    # Проверяем логирование некорректного номера
    invalid_card = "123"
    masked_invalid = mask_card_number(invalid_card)
    assert masked_invalid == "123"
    
    # Проверяем содержимое лог-файла
    with open("logs/masks.log", 'r', encoding='utf-8') as f:
        log_content = f.read()
        assert "INFO" in log_content
        assert "Номер карты 1234567890123456 успешно замаскирован" in log_content
        assert "WARNING" in log_content
        assert "Некорректный номер карты: 123" in log_content 