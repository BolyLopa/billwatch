# === Stage 85: Add final readiness report summarizing features and known limits ===
# Project: BillWatch
def print_readiness_report(bills):
    categories = sorted(set(b["category"] for b in bills))
    total_amount = sum(b["amount"] for b in bills)
    total_paid = sum(b["amount"] for b in bills if b["paid"])
    total_pending = sum(b["amount"] for b in bills if not b["paid"])
    due_soon = [b["description"] for b in bills if b["due"] and b["due"] <= _today()]
    overdue = [b["description"] for b in bills if not b["paid"] and b["due"] < _today()]

    print("BillWatch - Final Readiness Report")
    print("=" * 30)
    print(f"Total bills tracked : {len(bills)}")
    print(f"Categories          : {', '.join(categories) if categories else 'none'}")
    print(f"Total amount        : {total_amount:.2f}")
    print(f"Paid amount         : {total_paid:.2f}")
    print(f"Pending amount      : {total_pending:.2f}")
    print(f"Due soon            : {len(due_soon)}")
    print(f"Overdue             : {len(overdue)}")
    if due_soon:
        print("  Due soon:", due_soon)
    if overdue:
        print("  Overdue:", overdue)
    print("=" * 30)
    print("Features: due dates, payment status, categories, monthly summaries")
    print("Known limits: single-user, local file only, no notifications, no cloud sync")


def _today():
    from datetime import date
    return date.today()
