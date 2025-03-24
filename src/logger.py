import logging
import os
from datetime import datetime
from pathlib import Path


def setup_logger(name: str) -> logging.Logger:
    """
    Настраивает логгер для указанного модуля.
    
    Args:
        name: Имя модуля
        
    Returns:
        logging.Logger: Настроенный логгер
    """
    # Создаем директорию для логов, если она не существует
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Создаем имя файла лога
    log_file = log_dir / f"{name}.log"
    
    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Создаем форматтер для логов
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Создаем обработчик для записи в файл
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)
    
    return logger 