# === Stage 66: Add export of a short status dashboard ===
# Project: BillWatch
def export_status_dashboard(bills):
    from collections import defaultdict
    from datetime import date
    today = date.today()

    def is_paid(b):
        return b.get("status") == "paid"

    def overdue(b):
        due = b.get("due_date")
        if due and due < today and not is_paid(b):
            return True
        return False

    categories = defaultdict(list)
    for b in bills:
        categories[b.get("category", "Uncategorized")].append(b)

    print("BillWatch Status Dashboard")
    print("=" * 40)
    total = sum(float(b.get("amount", 0)) for b in bills)
    paid = sum(float(b.get("amount", 0)) for b in bills if is_paid(b))
    unpaid = total - paid
    print(f"Total Bills: {len(bills)}")
    print(f"Total Amount: ${total:.2f}")
    print(f"Paid: ${paid:.2f}")
    print(f"Unpaid: ${unpaid:.2f}")

    print("\nBy Category")
    print("-" * 40)
    for cat in sorted(categories):
        cat_bills = categories[cat]
        cat_total = sum(float(b.get("amount", 0)) for b in cat_bills)
        cat_unpaid = sum(float(b.get("amount", 0)) for b in cat_bills if not is_paid(b))
        print(f"{cat}: ${cat_total:.2f} (unpaid ${cat_unpaid:.2f})")

    print("\nOverdue Bills")
    print("-" * 40)
    overdue_bills = [b for b in bills if overdue(b)]
    if overdue_bills:
        for b in overdue_bills:
            due = b.get("due_date", "Unknown")
            print(f"{b.get('name', 'Bill')} - ${b.get('amount', 0):.2f} due {due}")
    else:
        print("No overdue bills.")
