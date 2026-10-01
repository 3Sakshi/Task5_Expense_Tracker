# Expense Tracker

## Project Overview
A Python-based Expense Tracker that allows users to record, view, search, analyze, and delete daily expenses.

The project uses JSON file storage so that expense data can be saved locally and loaded again when the application starts.


## Features
- Add a new expense
- View all expenses
- Calculate total expenses
- Calculate category-wise expenses
- Search expenses by category or description
- Delete an expense
- Input validation
- Error handling
- JSON-based data persistence
- Automated testing using pytest

## Project Structure
```text
Task5_Expense_Tracker/
│
├── main.py
├── expense_manager.py
├── models.py
├── validators.py
├── storage.py
└── test_expense_manager.py
```

## Technologies Used
- Python
- JSON
- Dataclasses
- pathlib
- pytest


## How to Run
Clone or download the repository.
Open the project folder in a terminal.
Run:
python main.py


## Menu Options
1. Add Expense
2. View All Expenses
3. View Total Expenses
4. Category-wise Total
5. Search Expenses
6. Delete Expense
7. Exit


## Data Storage
Expense data is stored locally in expenses.json.
The application automatically loads existing expenses when it starts and saves changes when expenses are added or deleted.


## Sample Usage
Example expense:
ID: 1
Category: Food
Amount: ₹150.00
Description: Lunch
Example output:
Total Expenses: ₹150.00
Total spent on food: ₹150.00


## Testing
The project includes automated tests using pytest.
Test command:
pytest -q
Test result:
8 passed in 0.83s
The tests cover:
- Adding expenses
- Total expense calculation
- Category-wise calculation
- Searching expenses
- Deleting expenses
- Duplicate expense IDs
- Invalid amounts
- Empty descriptions


## Error Handling
The application validates:
- Expense ID
- Category
- Amount
- Description
- Search keywords

Invalid inputs are handled using appropriate error messages instead of allowing the application to crash.


## Learning Outcomes
Through this project, I practiced:
- Python modular programming
- Object-oriented programming
- Dataclasses
- Input validation
- Exception handling
- JSON file handling
- Data processing
- Automated testing with pytest
- Organizing a Python project
- GitHub project management