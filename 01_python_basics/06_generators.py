transactions = [
    {"type": "income", "category": "salary", "amount": 50000},
    {"type": "expense", "category": "food", "amount": 3500},
    {"type": "expense", "category": "transport", "amount": 1200},
    {"type": "income", "category": "freelance", "amount": 15000},
]

def get_expenses(transactions):
    for transaction in transactions:
        if transaction["type"] == "expense":
            yield transaction

expenses = get_expenses(transactions)

for expense in expenses:
    print(expense)