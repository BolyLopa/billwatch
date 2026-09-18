# === Stage 40: Add plain text report export ===
# Project: BillWatch
def export_report(bills, months=None):
    """Export a plain text report of bills.

    Args:
        bills: list of bill dicts with keys: title, category, due_date,
               amount, paid, month, year.
        months: optional list of month strings to filter by.
    """
    if months is None:
        months = sorted(set(b['month'] for b in bills))
    lines = []
    lines.append("BillWatch Report")
    lines.append("=" * 40)
    for m in months:
        month_bills = [b for b in bills if b['month'] == m]
        lines.append(f"\n{m}")
        lines.append("-" * 20)
        for b in sorted(month_bills, key=lambda x: x['due_date']):
            status = "PAID" if b['paid'] else "PENDING"
            lines.append(f"  {b['title']:20s} | {b['category']:10s} | ${b['amount']:8.2f} | {b['due_date']} | {status}")
        total = sum(b['amount'] for b in month_bills)
        paid_total = sum(b['amount'] for b in month_bills if b['paid'])
        lines.append(f"  Total: ${total:8.2f}  Paid: ${paid_total:8.2f}")
    return "\n".join(lines)
