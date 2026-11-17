# === Stage 89: Add final consistency checks for names, statuses, and dates ===
# Project: BillWatch
def check_consistency(bills):
    valid_statuses = {"paid", "unpaid", "overdue", "partial"}
    for i, bill in enumerate(bills):
        name = bill.get("name")
        status = bill.get("status")
        due = bill.get("due_date")
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"Bill at index {i} has invalid name")
        if status not in valid_statuses:
            raise ValueError(f"Bill {name!r} has invalid status {status!r}")
        if due is not None:
            try:
                datetime.strptime(due, "%Y-%m-%d")
            except (TypeError, ValueError):
                raise ValueError(f"Bill {name!r} has invalid due_date {due!r}")
        if isinstance(bill.get("amount"), (int, float)) and bill["amount"] < 0:
            raise ValueError(f"Bill {name!r} has negative amount")
        return True
    return True
