# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: BillWatch
from dataclasses import dataclass
from datetime import date
from enum import Enum

class BillStatus(Enum):
    PENDING = "pending"
    OVERDUE = "overdue"
    PAID = "paid"

@dataclass
class Bill:
    name: str
    due_date: date
    amount: float
    category: str = "utilities"
    status: BillStatus = BillStatus.PENDING

    def is_overdue(self) -> bool:
        return self.status == BillStatus.PENDING and self.due_date < date.today()

    def total_due(self) -> float:
        return sum(b.amount for b in [self] if b.is_overdue())
