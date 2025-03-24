import unittest
from src.widget import mask_account_card, get_date


class TestMaskAccountCard(unittest.TestCase):

    def test_mask_visa(self):
        # Тестируем маску для Visa
        account_info = "Visa 1234-5678-9012-3456"
        expected_output = "Visa ****-****-****-3456"
        self.assertEqual(mask_account_card(account_info), expected_output)

    def test_mask_mastercard(self):
        # Тестируем маску для MasterCard
        account_info = "MasterCard 4321-8765-9876-5432"
        expected_output = "MasterCard ****-****-****-5432"
        self.assertEqual(mask_account_card(account_info), expected_output)

    def test_mask_maestro(self):
        # Тестируем маску для Maestro
        account_info = "Maestro 1111-2222-3333-4444"
        expected_output = "Maestro ****-****-****-4444"
        self.assertEqual(mask_account_card(account_info), expected_output)

    def test_mask_account(self):
        # Тестируем маску для счета
        account_info = "Счет 0987654321"
        expected_output = "Счет **********321"
        self.assertEqual(mask_account_card(account_info), expected_output)

    def test_invalid_input(self):
        # Проверяем исключение для неизвестного типа
        account_info = "Invalid Account Type 1234567890"
        with self.assertRaises(ValueError):
            mask_account_card(account_info)


class TestGetDate(unittest.TestCase):

    def test_valid_iso_format(self):
        # Тестируем корректное преобразование даты
        date_str = "2023-10-31T12:34:56+00:00"
        expected_output = "31.10.2023"
        self.assertEqual(get_date(date_str), expected_output)

    def test_invalid_iso_format(self):
        # Тестируем некорректную строку даты
        date_str = "invalid-date-format"
        expected_output = ""
        self.assertEqual(get_date(date_str), expected_output)


if __name__ == '__main__':
    unittest.main()