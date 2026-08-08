import json

from transaction import Transaction
from finance_tracker import FinanceTracker


if __name__ == "__main__":
    transactions = FinanceTracker()

    try:
        with open("transactions.json", mode="r", encoding="utf-8") as file:
            transactions_list = json.load(file)
            if not isinstance(transactions_list, list):
                raise TypeError("Транзакции должны находиться в списке")

            for transaction_data in transactions_list:
                if not isinstance(transaction_data, dict):
                    raise TypeError("Транзакция не является словарём")
                required_keys = ("type", "category", "amount")
                for key in required_keys:
                    if key not in transaction_data:
                        raise KeyError(f"Отсутствует обязательное поле: {key}")
                transaction = Transaction(transaction_data["type"], transaction_data["category"], transaction_data["amount"])
                transactions.add_transaction(transaction)
            
    except FileNotFoundError:
        print("Файл с транзакциями не найден")
    
    except json.JSONDecodeError:
        print("Файл содержит некорректный JSON")
    
    except (TypeError, ValueError, KeyError) as error:
        print(f"Ошибка данных: {error}")

    else:
        print(f"Доходы: {transactions.sum_income()}")
        print(f"Расходы: {transactions.sum_expense()}")
        print(f"Баланс: {transactions.get_balance()}")
        print(f"Самая крупная трата: {transactions.get_largest_expense()}")
        print()
        print("Расходы по категориям:")
        for category, amount in transactions.get_expenses_by_category().items():
            print(f"{category}: {amount}")
        print()
        print(f"Самая затратная категория: {transactions.get_most_expensive_category()}")
    