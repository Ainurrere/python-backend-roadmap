transactions = [
    {"type": "income", "category": "salary", "amount": 50000},
    {"type": "expense", "category": "food", "amount": 3500},
    {"type": "expense", "category": "transport", "amount": 1200},
    {"type": "income", "category": "freelance", "amount": 15000},
]


def enumerate_categories(transactions):
    categories = [
        transaction["category"]
        for transaction in transactions
    ]
    result = []
    for index, name in enumerate(categories, start=1):
        result.append((index, name))
    return result


def enumerate_expenses(transactions):
    expenses = [
        transaction["category"]
        for transaction in transactions
        if transaction["type"] == "expense"
    ]
    result = []
    for index, name in enumerate(expenses, start=1):
        result.append((index, name))

    return result


def enumerate_large_transactions(transactions):
    large_transactions = [
        (transaction["category"], transaction["amount"])
        for transaction in transactions
        if transaction["amount"] >= 10000
    ]
    result = []
    for index, (category, amount) in enumerate(large_transactions, start=1):
        result.append((index, category, amount))

    return result

def enumerate_expense_amounts(transactions):
    expense_amounts = [
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "expense"
    ]
    result = []
    for index, amount in enumerate(expense_amounts, start=1):
        result.append((index, amount))

    return result


def enumerate_income_categories(transactions):
    income_categories = [
        transaction["category"]
        for transaction in transactions
        if transaction["type"] == "income"
    ]
    result = []
    for index, category in enumerate(income_categories, start=1):
        result.append((index, category))

    return result


def enumerate_all_transactions(transactions):
    all_transactions = [
        (transaction["type"], transaction["category"], transaction["amount"])
        for transaction in transactions
    ]
    result = []
    for index, (type, category, amount) in enumerate(all_transactions, start=1):
        result.append((index, type, category, amount))

    return result


def enumerate_small_expenses(transactions):
    small_expenses = [
        transaction["category"]
        for transaction in transactions
        if transaction["type"] == "expense" and transaction["amount"] < 5000
    ]
    result = []
    for index, category in enumerate(small_expenses, start=1):
        result.append((index, category))

    return result


def enumerate_categories_from_5(transactions):
    categories = [
        transaction["category"] 
        for transaction in transactions
    ]
    result = []
    for index, category in enumerate(categories, start=5):
        result.append((index, category))

    return result


def enumerate_transaction_labels(transactions):
    transaction_labels = [
        "large" if transaction["amount"] >= 10000 else "small"
        for transaction in transactions
    ]
    result = []
    for index, label in enumerate(transaction_labels, start=1):
        result.append((index, label))

    return result


def enumerate_expense_labels(transactions):
    expense_labels = [
        (transaction["category"], "large" if transaction["amount"] >= 10000 else "small")
        for transaction in transactions
        if transaction["type"] == "expense"
    ]
    result = []
    for index, (category, label) in enumerate(expense_labels, start=1):
        result.append((index, category, label))

    return result


def enumerate_unique_categories(transactions):
    unique_categories = {
        transaction["category"]: None
        for transaction in transactions
    }
    result = []
    for index, category in enumerate(unique_categories, start=1):
        result.append((index, category))

    return result


def enumerate_transaction_pairs(transactions):
    transaction_pairs = [
        (transaction["category"], transaction["amount"])
        for transaction in transactions
    ]
    result = []
    for index, (category, amount) in enumerate(transaction_pairs, start=1):
        result.append((index, (category, amount)))

    return result



categories = ["salary", "food", "rent"]
amounts = [50000, 3500, 18000]


def combine_categories_and_amounts(categories, amounts):
    categories_and_amounts = []
    for category, amount in zip(categories, amounts):
        categories_and_amounts.append((category, amount))

    return categories_and_amounts


def make_category_dict(categories, amounts):
    result = dict(zip(categories, amounts))
    return result


def has_large_expense(transactions):
    result = any(
        transaction["type"] == "expense" and transaction["amount"] > 10000
        for transaction in transactions
    )
    return result


def all_amounts_positive(transactions):
    result = all(
        transaction["amount"] > 0
        for transaction in transactions
    )
    return result

print(all_amounts_positive(transactions))

