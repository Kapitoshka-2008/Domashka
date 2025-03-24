def filter_by_currency(transactions, currency_code):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start=1, stop=None):
    if not stop:
        stop = start + 1  # По умолчанию генерируем 10 тысяч карт
    for i in range(start, stop+1):
        card_number = f"{i:016d}"
        formatted_number = " ".join([card_number[i:i+4] for i in range(0, len(card_number), 4)])
        yield formatted_number