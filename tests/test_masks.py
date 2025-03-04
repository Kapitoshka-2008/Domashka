import unittest
from src import masks
from tests.conftest import short_card_number, long_card_number, account_number, empty_account_number, \
    card_number_and_expected


def test_mask_card_number_valid(card_number_and_expected):
    """Тест маски номера карты с использованием параметризации."""
    card_number, expected_output = card_number_and_expected
    assert masks.mask_card_number(card_number) == expected_output


def test_mask_card_number_short(short_card_number):
    """Тест короткой маски номера карты."""
    expected_output = "1234 56** **** 34"
    assert masks.mask_card_number(short_card_number) == expected_output


def test_mask_card_number_long(long_card_number):
    """Тест длинной маски номера карты."""
    expected_output = "1234 56** **** 34567890"
    assert masks.mask_card_number(long_card_number) == expected_output


def test_mask_account_number_valid(account_number):
    """Тест маски номера счета."""
    expected_output = "** 5678"
    assert masks.mask_account_number(account_number) == expected_output


def test_mask_account_number_empty(empty_account_number):
    """Тест пустой маски номера счета."""
    expected_output = "** "
    assert masks.mask_account_number(empty_account_number) == expected_output


if __name__ == "__main__":
    unittest.main()
