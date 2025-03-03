import unittest

from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator
)


class FilterByCurrencyTests(unittest.TestCase):
    """Тестирование функции фильтрации транзакций по коду валюты."""

    def test_usd_transactions(self):
        """Проверка фильтрации по валюте USD."""
        transactions = [
            {"operationAmount": {"currency": {"code": "USD"}}},
            {"operationAmount": {"currency": {"code": "EUR"}}},
            {"operationAmount": {"currency": {"code": "USD"}}}
        ]
        result = list(filter_by_currency(transactions, "USD"))
        expected_result = [transactions[0], transactions[2]]
        self.assertEqual(result, expected_result)

    def test_eur_transactions(self):
        """Проверка фильтрации по валюте EUR."""
        transactions = [
            {"operationAmount": {"currency": {"code": "USD"}}},
            {"operationAmount": {"currency": {"code": "EUR"}}},
            {"operationAmount": {"currency": {"code": "USD"}}}
        ]
        result = list(filter_by_currency(transactions, "EUR"))
        expected_result = [transactions[1]]
        self.assertEqual(result, expected_result)

    def test_no_matching_currency(self):
        """Проверка результата при отсутствии нужной валюты."""
        transactions = [
            {"operationAmount": {"currency": {"code": "USD"}}},
            {"operationAmount": {"currency": {"code": "EUR"}}},
            {"operationAmount": {"currency": {"code": "USD"}}}
        ]
        result = list(filter_by_currency(transactions, "RUB"))
        expected_result = []
        self.assertEqual(result, expected_result)


class TransactionDescriptionsTests(unittest.TestCase):
    """Тестирование функции получения описаний транзакций."""

    def test_with_descriptions(self):
        """Проверка описаний транзакций с наличием текста."""
        transactions = [
            {"description": "Покупка товара"},
            {},
            {"description": "Оплата услуги"}
        ]
        result = list(transaction_descriptions(transactions))
        expected_result = ["Покупка товара", "", "Оплата услуги"]
        self.assertEqual(result, expected_result)

    def test_empty_list(self):
        """Проверка пустого списка транзакций."""
        result = list(transaction_descriptions([]))
        expected_result = []
        self.assertEqual(result, expected_result)


class CardNumberGeneratorTests(unittest.TestCase):
    """Тестирование генератора номеров карт."""

    def test_default_generation(self):
        """Проверка базовой генерации номеров карт."""
        result = list(card_number_generator())
        self.assertIn('0000 0000 0000 0001', result)
        self.assertIn('0000 0000 0000 0002', result)
        self.assertEqual(len(result), 2)

    def test_range_generation(self):
        """Проверка генерации номеров карт с заданным диапазоном."""
        result = list(card_number_generator(5000, 6000))
        self.assertIn('0000 0000 0000 5000', result)
        self.assertIn('0000 0000 0000 5001', result)
        self.assertEqual(len(result), 1001)


if __name__ == '__main__':
    unittest.main()