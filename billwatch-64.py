# === Stage 64: Add validation for relationship references ===
# Project: BillWatch
def validate_references(bills, categories):
    """Ensure every bill references an existing category by id."""
    category_ids = {c["id"] for c in categories}
    for bill in bills:
        if not isinstance(bill, dict):
            raise ValueError(f"Bill is not a dict: {bill!r}")
        required = ["id", "name", "amount", "due_date", "category_id", "paid"]
        for field in required:
            if field not in bill:
                raise ValueError(f"Bill {bill.get('id')} missing field '{field}'")
        if not isinstance(bill["amount"], (int, float)):
            raise ValueError(f"Bill {bill['id']} has non-numeric amount")
        if isinstance(bill["due_date"], str):
            from datetime import datetime
            datetime.strptime(bill["due_date"], "%Y-%m-%d")
        if bill["category_id"] not in category_ids:
            raise ValueError(
                f"Bill {bill['id']} references unknown category_id "
                f"'{bill['category_id']}'"
            )
        if not isinstance(bill["paid"], bool):
            raise ValueError(f"Bill {bill['id']} has non-boolean paid flag")
    return bills
