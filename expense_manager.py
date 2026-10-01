from models import Expense
from validators import (
    validate_category,
    validate_amount,
    validate_description,
    validate_expense_id
)


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense_id, category, amount, description):
        expense_id = validate_expense_id(expense_id)
        category = validate_category(category)
        amount = validate_amount(amount)
        description = validate_description(description)

        if any(expense.expense_id == expense_id for expense in self.expenses):
            raise ValueError("An expense with this ID already exists.")

        expense = Expense(
            expense_id,
            category,
            amount,
            description
        )

        self.expenses.append(expense)
        return expense

    def get_all_expenses(self):
        return self.expenses

    def get_total_expenses(self):
        return round(
            sum(expense.amount for expense in self.expenses),
            2
        )

    def get_category_total(self, category):
        category = validate_category(category).lower()

        total = sum(
            expense.amount
            for expense in self.expenses
            if expense.category.lower() == category
        )

        return round(total, 2)

    def search_expenses(self, keyword):
        keyword = keyword.strip().lower()

        if not keyword:
            raise ValueError("Search keyword cannot be empty.")

        return [
            expense
            for expense in self.expenses
            if keyword in expense.category.lower()
            or keyword in expense.description.lower()
        ]

    def delete_expense(self, expense_id):
        expense_id = validate_expense_id(expense_id)

        for expense in self.expenses:
            if expense.expense_id == expense_id:
                self.expenses.remove(expense)
                return expense

        raise ValueError("Expense not found.")