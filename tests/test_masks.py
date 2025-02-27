import unittest

from src import masks
class MaskingTests(unittest.TestCase):

    def test_mask_card_number_valid(self):
        # Корректный номер карты длиной 16 символов
        card_number = "1234567890123456"
        expected_output = "1234 56** **** 3456"
        self.assertEqual(masks.mask_card_number(card_number), expected_output)

    def test_mask_card_number_short(self):
        # Неверная длина карты (меньше 16 символов)
        card_number = "12345678901234"
        expected_output = "12345678901234"
        self.assertEqual(masks.mask_card_number(card_number), expected_output)

    def test_mask_card_number_long(self):
        # Слишком длинная карта (больше 16 символов)
        card_number = "12345678901234567890"
        expected_output = "12345678901234567890"
        self.assertEqual(masks.mask_card_number(card_number), expected_output)

    def test_mask_account_number_valid(self):
        # Корректный номер счета (длина >= 4 символа)
        account_number = "12345678"
        expected_output = "**5678"
        self.assertEqual(masks.mask_account_number(account_number), expected_output)

    def test_mask_account_number_short(self):
        # Очень короткий номер счета (менее 4 символов)
        account_number = "**  123"
        expected_output = "**  123"
        self.assertEqual(masks.mask_account_number(account_number), expected_output)

    def test_mask_account_number_exact_length(self):
        # Точный номер счета длиной ровно 4 символа
        account_number = "1234"
        expected_output = "**34"
        self.assertEqual(masks.mask_account_number(account_number), expected_output)

if __name__ == "__main__":
    unittest.main()