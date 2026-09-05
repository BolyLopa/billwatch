# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: BillWatch
class Bill:
    def __init__(self, name, due_date, category, paid, amount):
        self.name = name
        self.due_date = due_date
        self.category = category
        self.paid = paid
        self.amount = amount

    def __repr__(self):
        return f"{self.name} | Due: {self.due_date} | {self.category} | {'Paid' if self.paid else 'Unpaid'} | ${self.amount:.2f}"
