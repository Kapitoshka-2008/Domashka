import unittest

from src.processing import filter_by_state, sort_by_date


class TestFilterByState(unittest.TestCase):

    def setUp(self):
        # Данные для тестирования
        self.data = [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
        ]

    def test_filter_by_state_executed(self):
        # Тестируем фильтрацию по состоянию EXECUTED
        result = filter_by_state(self.data, state="EXECUTED")
        expected_result = [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
        ]
        self.assertEqual(result, expected_result)

    def test_filter_by_state_canceled(self):
        # Тестируем фильтрацию по состоянию CANCELED
        result = filter_by_state(self.data, state="CANCELED")
        expected_result = [
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
        ]
        self.assertEqual(result, expected_result)

    def test_filter_empty_state(self):
        # Тестируем фильтрацию по несуществующему состоянию
        result = filter_by_state(self.data, state="UNKNOWN_STATE")
        expected_result = []
        self.assertEqual(result, expected_result)


class TestSortByDate(unittest.TestCase):

    def setUp(self):
        # Данные для тестирования
        self.data = [
            {"id": 1, "state": "A", "date": "2020-01-15T12:34:56.000000"},
            {"id": 2, "state": "B", "date": "2019-05-20T23:45:59.999999"},
            {"id": 3, "state": "C", "date": "2021-11-22T17:38:24.100000"},
            {"id": 4, "state": "D", "date": "2018-04-13T19:55:32.200000"}
        ]

    def test_sort_descending(self):
        # Тестируем сортировку по убыванию
        result = sort_by_date(self.data)
        expected_result = [
            {"id": 3, "state": "C", "date": "2021-11-22T17:38:24.100000"},
            {"id": 1, "state": "A", "date": "2020-01-15T12:34:56.000000"},
            {"id": 2, "state": "B", "date": "2019-05-20T23:45:59.999999"},
            {"id": 4, "state": "D", "date": "2018-04-13T19:55:32.200000"}
        ]
        self.assertEqual(result, expected_result)

    def test_sort_ascending(self):
        # Тестируем сортировку по возрастанию
        result = sort_by_date(self.data, order="ascending")
        expected_result = [
            {"id": 4, "state": "D", "date": "2018-04-13T19:55:32.200000"},
            {"id": 2, "state": "B", "date": "2019-05-20T23:45:59.999999"},
            {"id": 1, "state": "A", "date": "2020-01-15T12:34:56.000000"},
            {"id": 3, "state": "C", "date": "2021-11-22T17:38:24.100000"}
        ]
        self.assertEqual(result, expected_result)

    def test_sort_with_same_dates(self):
        # Тестируем сортировку, когда есть одинаковые даты
        same_date_data = [
            {"id": 1, "state": "A", "date": "2020-01-15T12:34:56.000000"},
            {"id": 2, "state": "B", "date": "2020-01-15T12:34:56.000000"},
            {"id": 3, "state": "C", "date": "2020-01-15T12:34:56.000000"}
        ]
        result = sort_by_date(same_date_data)
        expected_result = [
            {"id": 1, "state": "A", "date": "2020-01-15T12:34:56.000000"},
            {"id": 2, "state": "B", "date": "2020-01-15T12:34:56.000000"},
            {"id": 3, "state": "C", "date": "2020-01-15T12:34:56.000000"}
        ]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()