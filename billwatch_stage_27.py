# === Stage 27: Add monthly summary calculations ===
# Project: BillWatch
def monthly_summary(bills, month=None):
    """Generate a monthly summary from a list of bills.

    Args:
        bills: list of bill dicts with 'amount', 'due_date', 'status', 'category'
        month: optional string 'YYYY-MM' to filter; defaults to all bills

    Returns:
        dict with 'month', 'total', 'paid_total', 'pending_total', 'by_category'
    """
    if month:
        filtered = [b for b in bills if b['due_date'].startswith(month)]
    else:
        filtered = bills

    total = sum(b['amount'] for b in filtered)
    paid = sum(b['amount'] for b in filtered if b['status'] == 'paid')
    pending = total - paid

    by_category = {}
    for b in filtered:
        cat = b['category']
        by_category[cat] = by_category.get(cat, 0) + b['amount']

    return {
        'month': month,
        'total': total,
        'paid_total': paid,
        'pending_total': pending,
        'by_category': by_category,
    }
