# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: BillWatch
def format_bill(bill):
    status_icon = "✓" if bill["status"] == "paid" else "✗"
    return f"{status_icon} [{bill['category']}] {bill['description']:<25} due {bill['due_date']}  pay {bill['amount']}  status {bill['status']}"

def print_bills(bills):
    print(f"\n{'─'*60}")
    print(f"{'Category':<12} {'Description':<28} {'Due Date':<12} {'Amount':>8} {'Status':>6}")
    print(f"{'─'*60}")
    for b in bills:
        print(f"{b['category']:<12} {b['description']:<28} {b['due_date']:<12} {b['amount']:>8} {b['status']:<6}")
    print(f"{'─'*60}")

def print_monthly_summary(monthly):
    print(f"\n{'─'*60}")
    print(f"{'Month':<12} {'Total Bills':<14} {'Paid':<10} {'Unpaid':<10} {'Balance':>8}")
    print(f"{'─'*60}")
    for month, data in monthly.items():
        total = data['total']
        paid = data['paid']
        unpaid = data['unpaid']
        balance = total - paid
        print(f"{month:<12} {total:<14} {paid:<10} {unpaid:<10} {balance:>8}")
    print(f"{'─'*60}")
