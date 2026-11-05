# === Stage 67: Add a function that returns key project metrics ===
# Project: BillWatch
def project_metrics(bills, monthly_summaries):
    """Return key project metrics for BillWatch."""
    total_bills = len(bills)
    if total_bills == 0:
        return {
            "total_bills": 0,
            "total_amount": 0.0,
            "paid_amount": 0.0,
            "unpaid_amount": 0.0,
            "paid_percentage": 0.0,
            "categories": [],
        }

    total_amount = sum(b["amount"] for b in bills)
    paid_amount = sum(b["amount"] for b in bills if b["paid"])
    unpaid_amount = total_amount - paid_amount
    categories = sorted({b["category"] for b in bills})
    if total_amount > 0:
        paid_percentage = (paid_amount / total_amount) * 100
    else:
        paid_percentage = 0.0

    return {
        "total_bills": total_bills,
        "total_amount": round(total_amount, 2),
        "paid_amount": round(paid_amount, 2),
        "unpaid_amount": round(unpaid_amount, 2),
        "paid_percentage": round(paid_percentage, 1),
        "categories": categories,
    }
