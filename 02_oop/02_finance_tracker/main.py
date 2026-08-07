from transaction import Transaction
from finance_tracker import FinanceTracker


if __name__ == "__main__":
    salary = Transaction("income", "salary", 50000)
    food = Transaction("expense", "food", 3500)

    transactions = FinanceTracker()

    transactions.add_transaction(salary)
    transactions.add_transaction(food)

    print(transactions.transactions)
    summary_income = transactions.sum_income()
    print(summary_income)
    print(transactions.sum_expense())