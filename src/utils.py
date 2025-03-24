import json
from typing import List, Dict, Any
from pathlib import Path
from .logger import setup_logger

logger = setup_logger('utils')


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
            logger.warning(f"Файл {file_path} не найден")
            return []
            
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not isinstance(data, list):
            logger.warning(f"Файл {file_path} не содержит список транзакций")
            return []
            
        logger.info(f"Успешно загружено {len(data)} транзакций из файла {file_path}")
        return data
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка при разборе JSON файла {file_path}: {str(e)}")
        return []
    except Exception as e:
        logger.error(f"Неожиданная ошибка при загрузке файла {file_path}: {str(e)}")
        return [] 