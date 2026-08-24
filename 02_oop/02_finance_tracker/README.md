# FinanceTracker

Учебный консольный проект на Python для учёта доходов и расходов.

## Описание

FinanceTracker хранит финансовые операции в виде объектов `Transaction`, загружает данные из JSON-файла и позволяет получить основные показатели по доходам и расходам.

Проект создан для практики ООП, работы с файлами, обработки исключений и unit-тестирования с `pytest`.

## Возможности

- добавление доходов и расходов;
- подсчёт общей суммы доходов;
- подсчёт общей суммы расходов;
- расчёт текущего баланса;
- поиск самой крупной траты;
- подсчёт расходов по категориям;
- поиск самой затратной категории;
- загрузка транзакций из `transactions.json`;
- проверка корректности данных;
- unit-тесты для `Transaction` и `FinanceTracker`.

## Структура проекта

```text
02_finance_tracker/
├── transaction.py
├── finance_tracker.py
├── main.py
├── transactions.json
├── README.md
└── tests/
    ├── test_transaction.py
    └── test_finance_tracker.py
```

- `transaction.py` — класс `Transaction`, свойства, валидация и magic methods.
- `finance_tracker.py` — класс `FinanceTracker` и логика работы с транзакциями.
- `main.py` — загрузка JSON, создание объектов и вывод отчёта.
- `transactions.json` — тестовые данные.
- `tests/test_transaction.py` — тесты класса `Transaction`.
- `tests/test_finance_tracker.py` — тесты класса `FinanceTracker`.

## Запуск проекта

Из папки `02_finance_tracker`:

```bash
python main.py
```

## Запуск тестов

Установить pytest:

```bash
python -m pip install pytest
```

Запустить все тесты:

```bash
python -m pytest -v
```

## Что я изучил

В проекте применены:

- классы и объекты;
- `__init__` и `self`;
- свойства через `@property`;
- setter'ы и валидация данных;
- magic methods `__str__`, `__repr__`, `__eq__`;
- исключения `TypeError`, `ValueError`, `KeyError`;
- `try / except / else`;
- работа с JSON;
- чтение файлов через `with open`;
- unit-тестирование с `pytest`;
- обычный `assert`;
- `pytest.raises`;
- `@pytest.mark.parametrize`;
- pytest fixtures;
- проверка граничных случаев.
