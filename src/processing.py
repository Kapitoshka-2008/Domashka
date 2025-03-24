from typing import List, Dict, Any
from datetime import datetime


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по заданному состоянию.
    :param data: Список словарей
    :param state: Значение состояния, по которому будет производиться фильтрация (по умолчанию 'EXECUTED')
    :return: Новый список словарей, соответствующих указанному состоянию
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], order: str = "descending") -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.
    :param data: Список словарей
    :param order: Порядок сортировки ('ascending' или 'descending'; по умолчанию 'descending')
    :return: Отсортированный список словарей
    """
    # Преобразуем строки дат в объекты datetime для корректной сортировки
    for item in data:
        item["date"] = datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%f")

    # Определяем направление сортировки
    reverse = True if order.lower() == "descending" else False

    # Сортируем данные
    sorted_data = sorted(data, key=lambda x: x["date"], reverse=reverse)

    # Возвращаем даты обратно в строковый формат
    for item in sorted_data:
        item["date"] = item["date"].strftime("%Y-%m-%dT%H:%M:%S.%f")

    return sorted_data


data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Пример вызова функции filter_by_state
filtered_executed = filter_by_state(data)
print(filtered_executed)

# Пример вызова функции sort_by_date
sorted_descending = sort_by_date(data)
print(sorted_descending)
