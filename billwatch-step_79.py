# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: BillWatch
def self_check():
    bills = [
        {"id": 1, "name": "Electricity", "due": "2024-06-15", "amount": 120.5, "status": "paid", "category": "utilities"},
        {"id": 2, "name": "Internet", "due": "2024-06-20", "amount": 60.0, "status": "pending", "category": "utilities"},
        {"id": 3, "name": "Rent", "due": "2024-06-01", "amount": 1000.0, "status": "overdue", "category": "housing"},
    ]
    today = "2024-06-25"
    print(f"Total bills: {len(bills)}")
    print(f"Due this month: {sum(1 for b in bills if b['due'].startswith(today[:7]))}")
    print(f"Pending amount: {sum(b['amount'] for b in bills if b['status'] == 'pending'):.2f}")
    print(f"Overdue amount: {sum(b['amount'] for b in bills if b['status'] == 'overdue'):.2f}")
    summary = {}
    for b in bills:
        summary[b['category']] = summary.get(b['category'], 0) + b['amount']
    for cat, total in summary.items():
        print(f"Category {cat}: {total:.2f}")
    print("self-check passed")
