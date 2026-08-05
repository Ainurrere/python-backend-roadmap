from finance import (
    analyze_transactions,
    print_report,
    get_expenses_by_category,
    find_most_expensive_category
)


transactions = [
    {"type": "income", "category": "salary", "amount": 50000},
    {"type": "expense", "category": "food", "amount": 3500},
    {"type": "expense", "category": "transport", "amount": 1200},
    {"type": "income", "category": "freelance", "amount": 8000},
    {"type": "expense", "category": "food", "amount": 2100},
]

if __name__ == "__main__":
    report = analyze_transactions(transactions)
    expenses_by_category = get_expenses_by_category(transactions)
    most_expensive = find_most_expensive_category(expenses_by_category)
    print_report(report, expenses_by_category, most_expensive)