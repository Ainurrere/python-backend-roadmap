def analyze_transactions(transactions):
    total_income = 0
    total_expense = 0
    largest_expense = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            total_income += transaction["amount"]
        elif transaction["type"] == "expense":
            total_expense += transaction["amount"]
            if transaction["amount"] > largest_expense:
                largest_expense = transaction["amount"]
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense,
        "largest_expense": largest_expense
    }
    

transactions = [
    {"type": "income", "category": "salary", "amount": 50000},
    {"type": "expense", "category": "food", "amount": 3500},
    {"type": "expense", "category": "transport", "amount": 1200},
    {"type": "income", "category": "freelance", "amount": 8000},
    {"type": "expense", "category": "food", "amount": 2100},
]

report = analyze_transactions(transactions)
print("Доходы:", report["total_income"], "руб.")
print("Расходы:", report["total_expense"], "руб.")
print("Баланс:", report["balance"], "руб.")
print("Самая крупная трата:", report["largest_expense"], "руб.")