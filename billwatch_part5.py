# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: BillWatch
def update_bill(self, bill_id, **kwargs):
    """Update an existing bill's fields. Only provided fields are changed."""
    if bill_id not in self._bills:
        raise KeyError(f"Bill with id {bill_id} not found.")
    bill = self._bills[bill_id]
    for key, value in kwargs.items():
        if key not in bill.__slots__:
            raise ValueError(f"Unknown field '{key}'. Valid fields: {bill.__slots__}")
        setattr(bill, key, value)
    return bill

def delete_bill(self, bill_id):
    """Remove a bill by id. Returns None if the record does not exist."""
    if bill_id not in self._bills:
        raise KeyError(f"Bill with id {bill_id} not found.")
    del self._bills[bill_id]
    return None
