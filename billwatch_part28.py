# === Stage 28: Add overdue item detection based on due dates ===
# Project: BillWatch
def find_overdue(bills, today=None):
    """Return list of bills past their due date."""
    if today is None:
        today = datetime.date.today()
    overdue = []
    for b in bills:
        if b["due_date"] < today:
            overdue.append(b)
    return overdue
