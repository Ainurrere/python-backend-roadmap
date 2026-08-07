class Transaction:
    def __init__(self, transaction_type, category, amount):
        self.transaction_type = transaction_type
        self.category = category
        self.amount = amount

    def is_income(self):
        return self.transaction_type == "income"


    def is_expense(self):
        return self.transaction_type == "expense"


    def get_description(self):
        return (f"{self.transaction_type.capitalize()} | {self.category} | {self.amount}")

    def __str__(self):
        return f"{self.transaction_type.capitalize()} | {self.category} | {self.amount}"

    def __repr__(self):
        return f"Transaction(transaction_type={self.transaction_type!r}, category={self.category!r}, amount={self.amount!r})"

    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return False

        return self.transaction_type == other.transaction_type and self.category == other.category and self.amount == other.amount
    


    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("Сумма операции должна быть числом")

        if value <= 0:
            raise ValueError("Сумма операции должна быть больше нуля")
        
        self._amount = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Категория операции должна быть строкой")
        
        if not value.strip():
            raise ValueError("Категория операции пустая")
        
        self._category = value

    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        if value not in ("income", "expense"):
            raise ValueError("Недопустимый тип операции")

        self._transaction_type = value




salary = Transaction("income", "salary", 50000)
food = Transaction("expense", "food", 3500)
a = Transaction("income", "salary", 50000)

print(salary.is_income())
print(food.is_expense())
print(food)
print(repr(food))
print(a == salary)
