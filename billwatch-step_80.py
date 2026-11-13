# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: BillWatch
def show_bill_status(bills):
    if not bills:
        print("No bills are tracked yet. Add your first bill to get started.")
        return
    for bill in bills:
        if bill["paid"]:
            print(f"✓ {bill['name']} — {bill['amount']} paid")
        else:
            print(f"✗ {bill['name']} — {bill['amount']} due {bill['due']}")
