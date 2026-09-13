# === Stage 26: Add weekly summary calculations ===
# Project: BillWatch
def weekly_summary(bills):
    """Return a dict with weekly payment totals and overdue counts."""
    from datetime import datetime, timedelta, timezone
    now = datetime.now(timezone.utc).date()
    week_ends = [now - timedelta(days=d) for d in range(7)]
    summary = {f"Week {i+1}": {"paid": 0, "due": 0, "overdue": 0} for i in range(7)}
    for idx, we in enumerate(week_ends):
        week_total = 0
        week_due = 0
        week_overdue = 0
        for b in bills:
            if b["due_date"].date() == we and b["payment_status"] == "paid":
                week_total += b["amount"]
            if b["due_date"].date() == we:
                week_due += b["amount"]
                if b["payment_status"] == "overdue":
                    week_overdue += b["amount"]
        summary[f"Week {idx+1}"] = {"paid": week_total, "due": week_due, "overdue": week_overdue}
    return summary
