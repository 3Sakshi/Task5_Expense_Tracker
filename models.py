from dataclasses import dataclass


@dataclass
class Expense:
    expense_id: int
    category: str
    amount: float
    description: str