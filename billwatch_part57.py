# === Stage 57: Add structured result objects for command handlers ===
# Project: BillWatch
from dataclasses import dataclass
from typing import Optional

@dataclass
class BillResult:
    bill_id: int
    title: str
    due_date: str
    status: str
    category: str
    amount: float
    paid_date: Optional[str] = None

@dataclass
class SummaryResult:
    month: str
    total_spent: float
    bill_count: int
    overdue_count: int
