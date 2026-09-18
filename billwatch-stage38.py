# === Stage 38: Add data integrity checks for broken references ===
# Project: BillWatch
def check_integrity(bills):
    categories = set(b["category"] for b in bills if b.get("category"))
    valid_cats = {"utilities", "subscriptions", "loans", "insurance", "other"}
    for b in bills:
        if b.get("category") and b["category"] not in valid_cats:
            raise ValueError(f"Invalid category: {b['category']}")
    for b in bills:
        if b.get("due_date") and b["due_date"] < "2000-01-01":
            raise ValueError(f"Invalid due_date: {b['due_date']}")
    paid = {b["id"] for b in bills if b.get("status") == "paid"}
    for b in bills:
        if b.get("status") == "paid" and b["id"] not in paid:
            raise ValueError("Status 'paid' but no id match")
    return True
