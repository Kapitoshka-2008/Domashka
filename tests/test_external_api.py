import pytest
import requests
from unittest.mock import patch, Mock
from src.external_api import convert_to_rub


def test_convert_to_rub_rub():
    # Тест для транзакции в рублях
    transaction = {"amount": 100, "currency": "RUB"}
    result = convert_to_rub(transaction)
    assert result == 100.0


def test_convert_to_rub_usd():
    # Тест для транзакции в USD
    transaction = {"amount": 100, "currency": "USD"}
    mock_response = Mock()
    mock_response.json.return_value = {"result": 9000.0}
    
    with patch('src.external_api.API_KEY', 'test_key'), \
         patch('requests.get', return_value=mock_response):
        result = convert_to_rub(transaction)
        assert result == 9000.0


def test_convert_to_rub_eur():
    # Тест для транзакции в EUR
    transaction = {"amount": 100, "currency": "EUR"}
    mock_response = Mock()
    mock_response.json.return_value = {"result": 10000.0}
    
    with patch('src.external_api.API_KEY', 'test_key'), \
         patch('requests.get', return_value=mock_response):
        result = convert_to_rub(transaction)
        assert result == 10000.0


def test_convert_to_rub_api_error():
    # Тест для ошибки API
    transaction = {"amount": 100, "currency": "USD"}
    
    with patch('src.external_api.API_KEY', 'test_key'), \
         patch('requests.get', side_effect=requests.RequestException("API Error")):
        with pytest.raises(ValueError, match="Failed to convert currency"):
            convert_to_rub(transaction)


def test_convert_to_rub_missing_api_key():
    # Тест для отсутствующего API ключа
    transaction = {"amount": 100, "currency": "USD"}
    
    with patch('src.external_api.API_KEY', None):
        with pytest.raises(ValueError, match="API key not found"):
            convert_to_rub(transaction)


def test_convert_to_rub_invalid_amount():
    # Тест для некорректной суммы
    transaction = {"amount": "invalid", "currency": "USD"}
    
    with pytest.raises(ValueError):
        convert_to_rub(transaction) 