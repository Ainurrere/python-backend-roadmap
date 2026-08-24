import pytest

from transaction import Transaction


def test_create_transaction():
    transaction = Transaction("income", "salary", 50000)

    assert transaction.transaction_type == "income"
    assert transaction.category == "salary"
    assert transaction.amount == 50000


def test_is_income():
    transaction = Transaction("income", "salary", 50000)
    result = transaction.is_income()

    assert result is True


def test_is_expense():
    transaction = Transaction("expense", "food", 3500)
    result = transaction.is_expense()

    assert result is True


def test_empty_category_raises_value_error():
    with pytest.raises(ValueError):
        Transaction("income", "  ", 50000)


def test_type_category_raises_type_error():
    with pytest.raises(TypeError):
        Transaction("income", False, 50000)


def test_transaction_type_raises_value_error():
    with pytest.raises(ValueError):
        Transaction("transaction", "food", 3500)


def test_equal_transactions():
    a = Transaction("income", "salary", 50000)
    b = Transaction("income", "salary", 50000)

    assert a == b 


def test_not_equal_transactions():
    a = Transaction("income", "salary", 50000)
    b = Transaction("income", "salary", 10000)

    assert a != b


def test_transaction_not_equal_to_other_type():
    a = Transaction("income", "salary", 50000)
    b = "Привет"
    assert a != b


def test_str_transaction():
    transaction = Transaction("income", "salary", 50000)

    assert str(transaction) == f"{transaction.transaction_type.capitalize()} | {transaction.category} | {transaction.amount}"


def test_repr_transaction():
    transaction = Transaction("income", "salary", 50000)

    assert repr(transaction) == f"Transaction(transaction_type={transaction.transaction_type!r}, category={transaction.category!r}, amount={transaction.amount!r})"


def test_get_description():
    transaction = Transaction("income", "salary", 50000)
    a = transaction.get_description()

    assert a == f"{transaction.transaction_type.capitalize()} | {transaction.category} | {transaction.amount}"


def test_is_income_returns_false_for_expense():
    transaction = Transaction("expense", "food", 3500)
    result = transaction.is_income()

    assert result is False


def test_is_expense_returns_false_for_income():
    transaction = Transaction("income", "salary", 50000)
    result = transaction.is_expense()

    assert result is False


@pytest.mark.parametrize(
    "amount, expected_exception",
    [
        (0, ValueError),
        (-500, ValueError),
        ("Привет", TypeError),
        (True, TypeError),
    ]
)
def test_invalid_amount(amount, expected_exception):
    with pytest.raises(expected_exception):
        Transaction("income", "salary", amount)