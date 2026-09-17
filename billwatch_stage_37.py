# === Stage 37: Add recommendations for the next useful action ===
# Project: BillWatch
def get_monthly_summary(bills):
    """Summarize bills by month."""
    from collections import defaultdict
    monthly = defaultdict(lambda: {"count": 0, "total": 0, "overdue": 0})
    for bill in bills:
        month_key = bill["due_date"][:7]  # YYYY-MM
        monthly[month_key]["count"] += 1
        monthly[month_key]["total"] += bill["amount"]
        if bill["due_date"] < bill["paid_date"]:
            monthly[month_key]["overdue"] += 1
    return dict(sorted(monthly.items()))
