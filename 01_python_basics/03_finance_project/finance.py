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


def print_report(report, expenses_by_category, most_expensive):
    print("ФИНАНСОВЫЙ ОТЧЁТ", end="\n\n")
    print("Доходы:", report["total_income"], "руб.")
    print("Расходы:", report["total_expense"], "руб.")
    print("Баланс:", report["balance"], "руб.")
    print("Самая крупная трата:", report["largest_expense"], "руб.", end="\n\n")
    print("РАСХОДЫ ПО КАТЕГОРИЯМ", end="\n\n")

    for category, amount in expenses_by_category.items():
        print(f"{category}: {amount} руб.")

    print()
    print("Самая крупная категория по тратам:", most_expensive)
    

def get_expenses_by_category(transactions):
    expenses = {}

    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction["category"]
            amount = transaction["amount"]

            if category in expenses:
                expenses[category] += amount
            else:
                expenses[category] = amount

    return expenses


def find_most_expensive_category(expenses_by_category):
    most_expensive = None
    most_expensive_amount = 0
    for category, amount in expenses_by_category.items():
        if amount > most_expensive_amount:
            most_expensive_amount = amount
            most_expensive = category

    return most_expensive