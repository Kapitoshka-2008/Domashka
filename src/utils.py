import json
from typing import List, Dict, Any
from pathlib import Path


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает транзакции из JSON-файла.
    
    Args:
        file_path: Путь к JSON-файлу с транзакциями
        
    Returns:
        List[Dict[str, Any]]: Список транзакций или пустой список в случае ошибки
    """
    try:
        file_path = Path(file_path)
        if not file_path.exists():
            return []
            
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not isinstance(data, list):
            return []
            
        return data
    except (json.JSONDecodeError, TypeError):
        return [] 