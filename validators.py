def validate_category(category):
    if not category or not category.strip():
        raise ValueError("Category cannot be empty.")
    if not all(char.isalpha() or char.isspace() for char in category):
        raise ValueError("Category must contain only letters and spaces.")
    return category.strip()


def validate_amount(amount):
    try:
        value = float(amount)
    except (TypeError, ValueError):
        raise ValueError("Amount must be a valid number.")

    if value <= 0:
        raise ValueError("Amount must be greater than 0.")

    return round(value, 2)


def validate_description(description):
    if not description or not description.strip():
        raise ValueError("Description cannot be empty.")
    return description.strip()


def validate_expense_id(expense_id):
    try:
        value = int(expense_id)
    except (TypeError, ValueError):
        raise ValueError("Expense ID must be a number.")

    if value <= 0:
        raise ValueError("Expense ID must be a positive integer.")

    return value