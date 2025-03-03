import pytest
from src import masks


@pytest.fixture
def biblioteka():
    return "1234567890123456"


class TestMasking:

    def test_mask_card_number_valid(self, biblioteka):
        """Тест маски номера карты"""
        expected_output = "1234 56** **** 3456"
        assert masks.mask_card_number(biblioteka) == expected_output

    def test_mask_card_number_short(self):
        """Тест короткой маски номера карты"""
        card_number = "12345678901234"
        expected_output = "1234 56** **** 34"
        assert masks.mask_card_number(card_number) == expected_output

    def test_mask_card_number_long(self):
        """Тест длинной маски номера карты"""
        card_number = "12345678901234567890"
        expected_output = "1234 56** **** 34567890"
        assert masks.mask_card_number(card_number) == expected_output

    def test_mask_account_number_valid(self):
        """Тест маски номера счета"""
        account_number = "12345678"
        expected_output = "** 5678"
        assert masks.mask_account_number(account_number) == expected_output

    def test_mask_account_number_short(self):
        """Тест короткой маски номера счета"""
        account_number = "** 123"
        expected_output = "**  123"
        assert masks.mask_account_number(account_number) == expected_output

    def test_mask_account_number_exact_length(self):
        """Тест точной длины маски номера счета"""
        account_number = "1234"
        expected_output = "** 1234"
        assert masks.mask_account_number(account_number) == expected_output