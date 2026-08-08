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


    def get_balance(self):
        return self.sum_income() - self.sum_expense()


    def get_largest_expense(self):
        largest_expense = 0

        for transaction in self.transactions:
            if transaction.is_expense():
                if transaction.amount > largest_expense:
                    largest_expense = transaction.amount

        return largest_expense


    def get_expenses_by_category(self):
        expenses_by_category = {}

        for transaction in self.transactions:
            if transaction.is_expense():
                if transaction.category in expenses_by_category:
                    expenses_by_category[transaction.category] += transaction.amount
                else:
                    expenses_by_category[transaction.category] = transaction.amount

        return expenses_by_category


    def get_most_expensive_category(self):
        expenses_by_category = self.get_expenses_by_category()
        most_expensive_amount = 0
        most_expensive_category = None

        for key, expense in expenses_by_category.items():
            if expense > most_expensive_amount:
                most_expensive_amount = expense
                most_expensive_category = key

        return most_expensive_category

