# === Stage 81: Add final README text as a module string with usage examples ===
# Project: BillWatch
BILLS = [
    {"id": 1, "name": "Electricity", "due": "2024-02-15", "status": "paid", "amount": 120.50, "category": "Utilities"},
    {"id": 2, "name": "Internet", "due": "2024-02-20", "status": "pending", "amount": 60.00, "category": "Utilities"},
    {"id": 3, "name": "Rent", "due": "2024-02-01", "status": "paid", "amount": 1500.00, "category": "Housing"},
]

def add_bill(name, due, amount, category="General"):
    bill = {"id": len(BILLS) + 1, "name": name, "due": due, "status": "pending", "amount": amount, "category": category}
    BILLS.append(bill)
    return bill

def mark_paid(bill_id):
    for bill in BILLS:
        if bill["id"] == bill_id:
            bill["status"] = "paid"
            return bill
    return None

def monthly_summary(month="2024-02"):
    year, m = map(int, month.split("-"))
    month_bills = [b for b in BILLS if b["due"].startswith(month)]
    total = sum(b["amount"] for b in month_bills)
    paid = sum(b["amount"] for b in month_bills if b["status"] == "paid")
    pending = total - paid
    return {"month": month, "total": total, "paid": paid, "pending": pending, "count": len(month_bills)}

def category_breakdown(month="2024-02"):
    summary = {}
    for b in BILLS:
        if b["due"].startswith(month):
            summary[b["category"]] = summary.get(b["category"], 0) + b["amount"]
    return summary

if __name__ == "__main__":
    print("Add bill:", add_bill("Water", "2024-02-10", 45.00, "Utilities"))
    print("Mark 2 paid:", mark_paid(2))
    print("Monthly summary:", monthly_summary("2024-02"))
    print("Category breakdown:", category_breakdown("2024-02"))
