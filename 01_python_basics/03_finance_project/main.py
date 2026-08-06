import json

from finance import (
    analyze_transactions,
    print_report,
    get_expenses_by_category,
    find_most_expensive_category,
    validate_transaction,
)


if __name__ == "__main__":
    try:
        with open("transactions.json", mode="r", encoding="utf-8") as file:
            transactions = json.load(file)
            if not isinstance(transactions, list):
                raise TypeError("Транзакции должны находиться в списке")
    
        for transaction in transactions:
            validate_transaction(transaction)
    except FileNotFoundError:
        print("Файл с транзакциями не найден")

    except json.JSONDecodeError:
        print("Файл содержит некорректный JSON")

    except (TypeError, ValueError) as error:
        print(f"Ошибка данных: {error}")

    else:
        report = analyze_transactions(transactions)
        expenses_by_category = get_expenses_by_category(transactions)
        most_expensive = find_most_expensive_category(expenses_by_category)
        print_report(report, expenses_by_category, most_expensive)