# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: BillWatch
def repair(bills):
    """Fix common data integrity issues in the bills list."""
    fixed = 0
    for i, bill in enumerate(bills):
        if not isinstance(bill, dict):
            continue
        # Ensure required fields exist
        for field in ["description", "due_date", "amount", "category", "paid"]:
            if field not in bill:
                bill[field] = None
        # Coerce amount to float, defaulting to 0.0
        if bill["amount"] is None:
            bill["amount"] = 0.0
        else:
            try:
                bill["amount"] = float(bill["amount"])
            except (TypeError, ValueError):
                bill["amount"] = 0.0
        # Normalize category to lowercase and strip whitespace
        if bill["category"] is None:
            bill["category"] = "uncategorized"
        else:
            try:
                bill["category"] = str(bill["category"]).strip().lower()
            except Exception:
                bill["category"] = "uncategorized"
        # Ensure due_date is a string (date format)
        if bill["due_date"] is None:
            bill["due_date"] = ""
        else:
            bill["due_date"] = str(bill["due_date"]).strip()
        # Normalize paid to boolean
        if bill["paid"] is None:
            bill["paid"] = False
        else:
            bill["paid"] = bool(bill["paid"])
        fixed += 1
    return bills
