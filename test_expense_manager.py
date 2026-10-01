from expense_manager import ExpenseManager


def test_add_expense():
    manager = ExpenseManager()

    expense = manager.add_expense(
        1,
        "Food",
        150,
        "Lunch"
    )

    assert expense.expense_id == 1
    assert expense.category == "Food"
    assert expense.amount == 150.0
    assert expense.description == "Lunch"


def test_total_expenses():
    manager = ExpenseManager()

    manager.add_expense(1, "Food", 150, "Lunch")
    manager.add_expense(2, "Travel", 100, "Bus")

    assert manager.get_total_expenses() == 250.0


def test_category_total():
    manager = ExpenseManager()

    manager.add_expense(1, "Food", 150, "Lunch")
    manager.add_expense(2, "Food", 200, "Dinner")
    manager.add_expense(3, "Travel", 100, "Bus")

    assert manager.get_category_total("Food") == 350.0
    assert manager.get_category_total("Travel") == 100.0


def test_search_expenses():
    manager = ExpenseManager()

    manager.add_expense(1, "Food", 150, "Lunch")
    manager.add_expense(2, "Travel", 100, "Bus ticket")

    results = manager.search_expenses("Lunch")

    assert len(results) == 1
    assert results[0].description == "Lunch"


def test_delete_expense():
    manager = ExpenseManager()

    manager.add_expense(1, "Food", 150, "Lunch")
    deleted = manager.delete_expense(1)

    assert deleted.expense_id == 1
    assert len(manager.expenses) == 0


def test_duplicate_expense_id():
    manager = ExpenseManager()

    manager.add_expense(1, "Food", 150, "Lunch")

    try:
        manager.add_expense(1, "Travel", 100, "Bus")
        assert False
    except ValueError:
        assert True


def test_invalid_amount():
    manager = ExpenseManager()

    try:
        manager.add_expense(
            1,
            "Food",
            -100,
            "Invalid expense"
        )
        assert False
    except ValueError:
        assert True


def test_empty_description():
    manager = ExpenseManager()

    try:
        manager.add_expense(
            1,
            "Food",
            100,
            ""
        )
        assert False
    except ValueError:
        assert True