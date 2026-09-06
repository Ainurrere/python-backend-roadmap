transactions = [
    {"type": "income", "category": "salary", "amount": 50000},
    {"type": "expense", "category": "food", "amount": 3500},
    {"type": "expense", "category": "transport", "amount": 1200},
    {"type": "income", "category": "freelance", "amount": 15000},
    {"type": "expense", "category": "rent", "amount": 18000},
    {"type": "expense", "category": "education", "amount": 4200},
]


def get_expensive_transactions(transactions):
    expensive_transactions = [
       transaction
       for transaction in transactions
       if transaction["amount"] > 3000
    ]
    return expensive_transactions


def get_expense_amounts(transactions):
    expense_amounts = [
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "expense"
    ]
    return expense_amounts


def get_unique_categories(transactions):
    categories = [
        transaction["category"]
        for transaction in transactions
    ]

    unique_categories = {category for category in categories}
    return unique_categories


def get_category_amounts(transactions):
    transaction_by_category = {
        transaction["category"]: transaction["amount"] for transaction in transactions
    }
    return transaction_by_category


def get_large_expense_categories(transactions):
    large_expense_categories = {
        transaction["category"]
        for transaction in transactions
        if transaction["type"] == "expense" and transaction["amount"] > 5000 
    }
    return large_expense_categories


def classify_amounts(transactions):
    class_amounts = [
        "large" if transaction["amount"] >= 10000 else "small"
        for transaction in transactions
    ]
    return class_amounts


def get_expensive_expense_amounts(transactions):
    expensive_expense_amounts = [
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "expense" and transaction["amount"] >= 4000
    ]
    return expensive_expense_amounts


def get_category_labels(transactions):
    category_labels = {
        transaction["category"]: "large" if transaction["amount"] >= 10000 else "small"
        for transaction in transactions
    }
    return category_labels


def get_transaction_pairs(transactions):
    transaction_pairs = [
        (transaction["category"], transaction["amount"])
        for transaction in transactions
    ]
    return transaction_pairs


sentences = [
    ["python", "backend"],
    ["sql", "postgresql"],
    ["fastapi", "docker"],
]


def get_all_words(sentences):
    all_words = [
        word
        for line in sentences
        for word in line
    ]
    return all_words


def get_long_words(sentences):
    long_words = [
        word
        for line in sentences
        for word in line
        if len(word) > 5
    ]
    return long_words    

print(get_long_words(sentences))