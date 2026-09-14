# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: BillWatch
def get_upcoming_bills(bills, days_ahead=7):
    """Return bills due within the next N days, sorted by due date."""
    today = datetime.date.today()
    upcoming = []
    for bill in bills:
        if bill["due_date"] and bill["due_date"] >= today and bill["due_date"] <= today + timedelta(days=days_ahead):
            upcoming.append(bill)
    upcoming.sort(key=lambda b: b["due_date"])
    return upcoming

def get_overdue_bills(bills):
    """Return bills past due, sorted by due date ascending."""
    today = datetime.date.today()
    overdue = [b for b in bills if b["due_date"] and b["due_date"] < today and not b["paid"]]
    overdue.sort(key=lambda b: b["due_date"])
    return overdue

def get_monthly_summary(bills, year=None, month=None):
    """Return a dict with per-category counts and totals for a given month."""
    today = datetime.date.today()
    if year is None and month is None:
        year, month = today.year, today.month
    month_start = datetime.date(year, month, 1)
    month_end = month_start.replace(day=28) + datetime.timedelta(days=4)
    month_end = month_end.replace(day=1) - datetime.timedelta(days=1)
    monthly = {
        "month": f"{year}-{month:02d}",
        "total_count": 0,
        "total_amount": 0.0,
        "by_category": {}
    }
    for bill in bills:
        if bill["due_date"] and month_start <= bill["due_date"] <= month_end:
            monthly["total_count"] += 1
            monthly["total_amount"] += bill.get("amount", 0)
            cat = bill.get("category", "Other")
            if cat not in monthly["by_category"]:
                monthly["by_category"][cat] = {"count": 0, "amount": 0.0}
            monthly["by_category"][cat]["count"] += 1
            monthly["by_category"][cat]["amount"] += bill.get("amount", 0)
    return monthly
