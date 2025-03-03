import unittest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

class TestFunctions(unittest.TestCase):

    def test_filter_by_currency(self):
        """Тестируем функцию фильтрации транзакций по коду валюты."""

        # Тестовые данные
        transactions = [
            {"operationAmount": {"currency": {"code": "USD"}}},
            {"operationAmount": {"currency": {"code": "EUR"}}},
            {"operationAmount": {"currency": {"code": "USD"}}}
        ]

        # Проверяем результат фильтрации по валюте USD
        result = list(filter_by_currency(transactions, "USD"))
        expected_result = [transactions[0], transactions[2]]
        self.assertEqual(result, expected_result)

        # Проверяем результат фильтрации по валюте EUR
        result = list(filter_by_currency(transactions, "EUR"))
        expected_result = [transactions[1]]
        self.assertEqual(result, expected_result)

        # Проверяем пустой список при отсутствии нужной валюты
        result = list(filter_by_currency(transactions, "RUB"))
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_transaction_descriptions(self):
        """Тестируем функцию получения описаний транзакций."""

        # Тестовые данные
        transactions = [
            {"description": "Покупка товара"},
            {},
            {"description": "Оплата услуги"}
        ]

        # Проверяем результат получения описаний
        result = list(transaction_descriptions(transactions))
        expected_result = ["Покупка товара", "", "Оплата услуги"]
        self.assertEqual(result, expected_result)

        # Проверяем корректное поведение при пустом списке транзакций
        result = list(transaction_descriptions([]))
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_card_number_generator(self):
        """Тестируем генератор номеров карт."""

        # Проверяем базовую генерацию номеров карт
        result = list(card_number_generator())
        # expected_result = ['0000 0100 0000 0010','0000 0000 0000 0001', '0000 0000 0000 0002', ..., '0000 0100 0000 0010']
        self.assertIn('0000 0000 0000 0001', result)
        self.assertIn('0000 0000 0000 0002', result)
        self.assertEqual(len(result), 2)

        # Проверяем генерацию номеров карт с заданным диапазоном
        result = list(card_number_generator(5000, 6000))
        # expected_result = ['0000 0100 0000 0010','0000 0050 0000 0000', '0000 0050 0000 0001', ..., '0000 0060 0000 0000']
        self.assertIn('0000 0000 0000 5000', result)
        self.assertIn('0000 0000 0000 5001', result)
        self.assertEqual(len(result), 1001)