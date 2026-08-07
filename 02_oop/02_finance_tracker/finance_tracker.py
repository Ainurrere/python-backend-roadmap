class FinanceTracker:
    def __init__(self):
        self.transactions = []


    def add_transaction(self, transaction):
        self.transactions.append(transaction)


    def sum_income(self):
        summary = 0

        for transaction in self.transactions:
            if transaction.is_income():
                summary += transaction.amount

        return summary


    def sum_expense(self):
        expenses = 0

        for transaction in self.transactions:
            if transaction.is_expense():
                expenses += transaction.amount

        return expenses
    