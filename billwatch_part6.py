# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: BillWatch
def delete_bill(bill_id, confirm=False):
    """Delete a bill by ID. Returns (success, message)."""
    if not confirm:
        return False, "Deletion requires confirmation flag set to True."
    if bill_id not in bills:
        return False, f"Bill {bill_id} not found."
    del bills[bill_id]
    return True, f"Bill {bill_id} deleted."
