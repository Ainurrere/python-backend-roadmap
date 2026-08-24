import pytest

from finance_tracker import FinanceTracker
from transaction import Transaction


@pytest.fixture
def finance_tracker():
    tracker = FinanceTracker()
    transaction_1 = Transaction("income", "salary", 50000)
    transaction_2 = Transaction("expense", "food", 1000)
    transaction_3 = Transaction("income", "salary", 10000)
    transaction_4 = Transaction("expense", "food", 3500)

    tracker.add_transaction(transaction_1)
    tracker.add_transaction(transaction_2)
    tracker.add_transaction(transaction_3)
    tracker.add_transaction(transaction_4)

    return tracker


@pytest.fixture
def category_tracker():
    tracker = FinanceTracker()
    transaction_1 = Transaction("expense", "rent", 18000) 
    transaction_2 = Transaction("expense", "food", 1000) 
    transaction_3 = Transaction("expense", "transport", 10000)
    transaction_4 = Transaction("expense", "food", 3500)

    tracker.add_transaction(transaction_1)
    tracker.add_transaction(transaction_2)
    tracker.add_transaction(transaction_3)
    tracker.add_transaction(transaction_4)

    return tracker 


@pytest.fixture
def empty_tracker():
    tracker = FinanceTracker()
    return tracker


def test_add_transaction():
    finance_tracker = FinanceTracker()
    transaction = Transaction("income", "salary", 30000)
    finance_tracker.add_transaction(transaction)
    assert len(finance_tracker.transactions) == 1


def test_sum_income(finance_tracker):
    income_sum = finance_tracker.sum_income()
    assert income_sum == 60000


def test_sum_expense(finance_tracker):
    expense_sum = finance_tracker.sum_expense()
    assert expense_sum == 4500


def test_get_balance(finance_tracker):
    balance = finance_tracker.get_balance()
    assert balance == 55500   


def test_get_largest_expense(finance_tracker):
    largest_expense = finance_tracker.get_largest_expense()
    assert largest_expense == 3500


def test_get_expenses_by_category(category_tracker):
    expenses_by_category = category_tracker.get_expenses_by_category()
    assert expenses_by_category["rent"] == 18000 and expenses_by_category["food"] == 4500 and expenses_by_category["transport"] == 10000


def test_get_most_expensive_category(category_tracker):
    most_expensive_category = category_tracker.get_most_expensive_category()
    assert most_expensive_category == "rent"   


def test_empty_tracker_sum_income(empty_tracker):
    income_sum = empty_tracker.sum_income()
    assert income_sum == 0


def test_empty_tracker_sum_expense(empty_tracker):
    expense_sum = empty_tracker.sum_expense()
    assert expense_sum == 0    


def test_empty_tracker_balance(empty_tracker):
    balance = empty_tracker.get_balance()
    assert balance == 0


def test_empty_tracker_most_expensive_category(empty_tracker):
    most_expensive_category = empty_tracker.get_most_expensive_category()
    assert most_expensive_category is None


def test_empty_tracker_largest_expense(empty_tracker):
    largest_expense = empty_tracker.get_largest_expense()
    assert largest_expense == 0


def test_empty_tracker_expenses_by_category(empty_tracker):
    expenses_by_category = empty_tracker.get_expenses_by_category()
    assert not expenses_by_category 


def test_add_transaction_stores_correct_transaction():
    tracker = FinanceTracker()
    transaction = Transaction("income", "salary", 50000)
    tracker.add_transaction(transaction)
    transaction_1 = tracker.transactions[0]
    assert transaction_1 is transaction


    