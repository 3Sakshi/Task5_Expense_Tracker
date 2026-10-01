from expense_manager import ExpenseManager
from storage import load_expenses, save_expenses
from validators import (
    validate_category,
    validate_amount,
    validate_description,
    validate_expense_id
)


def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n========== Expenses ==========")

    for expense in expenses:
        print(
            f"ID: {expense.expense_id} | "
            f"Category: {expense.category} | "
            f"Amount: ₹{expense.amount:.2f} | "
            f"Description: {expense.description}"
        )


def get_expense_id():
    while True:
        try:
            return validate_expense_id(
                input("Enter expense ID: ")
            )
        except ValueError as error:
            print(f"Error: {error}")


def add_expense(manager):
    try:
        expense_id = get_expense_id()

        category = validate_category(
            input("Enter category: ")
        )

        amount = validate_amount(
            input("Enter amount: ")
        )

        description = validate_description(
            input("Enter description: ")
        )

        expense = manager.add_expense(
            expense_id,
            category,
            amount,
            description
        )

        save_expenses(manager.expenses)

        print(
            f"Expense added successfully: "
            f"₹{expense.amount:.2f}"
        )

    except ValueError as error:
        print(f"Error: {error}")


def search_expenses(manager):
    keyword = input("Enter search keyword: ")

    try:
        results = manager.search_expenses(keyword)
        display_expenses(results)
    except ValueError as error:
        print(f"Error: {error}")


def show_category_total(manager):
    try:
        category = validate_category(
            input("Enter category: ")
        )

        total = manager.get_category_total(category)

        print(
            f"\nTotal spent on {category}: "
            f"₹{total:.2f}"
        )

    except ValueError as error:
        print(f"Error: {error}")


def delete_expense(manager):
    expense_id = get_expense_id()

    try:
        expense = manager.delete_expense(expense_id)
        save_expenses(manager.expenses)

        print(
            f"Expense '{expense.description}' "
            f"deleted successfully."
        )

    except ValueError as error:
        print(f"Error: {error}")


def main():
    manager = ExpenseManager()
    manager.expenses = load_expenses()

    while True:
        print("\n========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Category-wise Total")
        print("5. Search Expenses")
        print("6. Delete Expense")
        print("7. Exit")
        print("=====================================")

        choice = input("Enter your choice (1-7): ").strip()

        try:
            choice = int(choice)

            if choice == 1:
                add_expense(manager)

            elif choice == 2:
                display_expenses(
                    manager.get_all_expenses()
                )

            elif choice == 3:
                total = manager.get_total_expenses()
                print(
                    f"\nTotal Expenses: ₹{total:.2f}"
                )

            elif choice == 4:
                show_category_total(manager)

            elif choice == 5:
                search_expenses(manager)

            elif choice == 6:
                delete_expense(manager)

            elif choice == 7:
                print(
                    "\nThank you for using Expense Tracker."
                )
                break

            else:
                print(
                    "Invalid choice. "
                    "Please select a number from 1 to 7."
                )

        except ValueError:
            print("Error: Choice must be a number.")


if __name__ == "__main__":
    main()