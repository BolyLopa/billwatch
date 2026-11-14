# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: BillWatch
def demo_billwatch():
    bills = [
        {"id": 1, "name": "Electricity", "due_date": "2024-02-15",
         "status": "paid", "amount": 120.5},
        {"id": 2, "name": "Internet", "due_date": "2024-02-20",
         "status": "pending", "amount": 60.0},
        {"id": 3, "name": "Water", "due_date": "2024-02-25",
         "status": "overdue", "amount": 45.75},
    ]
    for b in bills:
        print(f"[{b['id']}] {b['name']} - due {b['due_date']} - "
              f"status: {b['status']} - ${b['amount']}")
    print("-" * 40)
    print("Monthly summary:")
    total = sum(b["amount"] for b in bills)
    pending = [b for b in bills if b["status"] != "paid"]
    print(f"Total bills: {len(bills)}")
    print(f"Total amount: ${total}")
    print(f"Pending/overdue: {len(pending)}")
    for b in pending:
        print(f"  - {b['name']}: ${b['amount']} (due {b['due_date']})")
    print("-" * 40)
    print("Demo complete. BillWatch tracking active for February 2024.")
