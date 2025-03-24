import pytest

@pytest.fixture
def biblioteka():
    return "1234567890123456"

@pytest.fixture(params=[
    ("1234567890123456", "1234 56** **** 3456"),  # Тест 1: Полная длина карты
    ("12345678901234", "1234 56** **** 34"),       # Тест 2: Короткая карта
    ("12345678901234567890", "1234 56** **** 34567890")  # Тест 3: Длинная карта
])
def card_number_and_expected(request):
    """Фикстура для предоставления номера карты и ожидаемого результата."""
    return request.param

@pytest.fixture
def short_card_number():
    """Фикстура для коротких номеров карт."""
    return "12345678901234"

@pytest.fixture
def long_card_number():
    """Фикстура для длинных номеров карт."""
    return "12345678901234567890"

@pytest.fixture
def account_number():
    """Фикстура для предоставления номера счета."""
    return "12345678"

@pytest.fixture
def empty_account_number():
    """Фикстура для пустых номеров счетов."""
    return ""
