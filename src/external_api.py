import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATES_API_KEY')
BASE_URL = 'https://api.apilayer.com/exchangerates_data/convert'


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    
    Args:
        transaction: Словарь с данными транзакции
        
    Returns:
        float: Сумма транзакции в рублях
    """
    amount = float(transaction.get('amount', 0))
    currency = transaction.get('currency', 'RUB')
    
    if currency == 'RUB':
        return amount
        
    if not API_KEY:
        raise ValueError("API key not found in environment variables")
        
    try:
        response = requests.get(
            BASE_URL,
            params={
                'apikey': API_KEY,
                'from': currency,
                'to': 'RUB',
                'amount': amount
            }
        )
        response.raise_for_status()
        result = response.json()
        return float(result['result'])
    except (requests.RequestException, KeyError, ValueError) as e:
        raise ValueError(f"Failed to convert currency: {str(e)}") 