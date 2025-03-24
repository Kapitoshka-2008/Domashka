import json
from typing import List, Dict, Any
from pathlib import Path
from .logger import setup_logger
from .file_handlers import read_transactions

logger = setup_logger(__name__)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает транзакции из файла.
    
    Args:
        file_path: Путь к файлу с транзакциями (поддерживаются форматы JSON, CSV, XLSX)
        
    Returns:
        Список словарей с транзакциями
    """
    file_path = Path(file_path)
    if not file_path.exists():
        logger.warning(f"Файл не найден: {file_path}")
        return []
        
    try:
        if file_path.suffix.lower() == '.json':
            logger.info(f"Начало чтения JSON файла: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not isinstance(data, list):
                    logger.warning(f"Данные в файле {file_path} не являются списком")
                    return []
                logger.info(f"Успешно загружено {len(data)} транзакций из JSON файла")
                return data
        else:
            return read_transactions(str(file_path))
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON файла {file_path}: {str(e)}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {str(e)}")
        return [] 