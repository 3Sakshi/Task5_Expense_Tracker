import json
from pathlib import Path
from models import Expense


DATA_FILE = Path(__file__).parent / "expenses.json"


def save_expenses(expenses):
    data = [
        {
            "expense_id": expense.expense_id,
            "category": expense.category,
            "amount": expense.amount,
            "description": expense.description
        }
        for expense in expenses
    ]

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_expenses():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [
            Expense(
                expense_id=item["expense_id"],
                category=item["category"],
                amount=item["amount"],
                description=item["description"]
            )
            for item in data
        ]

    except (json.JSONDecodeError, KeyError, TypeError):
        return []