# === Stage 25: Add daily summary calculations ===
# Project: BillWatch
def daily_summary(bills):
    """Compute per-day totals for a list of paid bills.

    Args:
        bills: list of dicts with keys 'paid_date' (str, YYYY-MM-DD)
               and 'amount' (float).

    Returns:
        dict mapping date string to total amount paid that day.
    """
    daily = {}
    for bill in bills:
        date = bill["paid_date"]
        amount = bill["amount"]
        daily[date] = daily.get(date, 0.0) + amount
    return daily
