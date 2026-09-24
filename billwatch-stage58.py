# === Stage 58: Add bulk update behavior for selected records ===
# Project: BillWatch
def bulk_update_records(records_to_update: dict) -> dict:
    """
    Bulk update selected records in the BillWatch tracker.
    
    Args:
        records_to_update (dict): Dictionary mapping record IDs (or names) to 
            updated field values. Example:
            {
                "electricity": {"due_date": "2024-02-15", "status": "paid"},
                "water": {"status": "paid"},
            }
    
    Returns:
        dict: Updated records with their new values.
    """
    updated = {}
    for record_id, new_values in records_to_update.items():
        if record_id not in tracker_data:
            print(f"Warning: Record '{record_id}' not found, skipping.")
            continue
        existing = tracker_data[record_id]
        existing.update(new_values)
        updated[record_id] = existing
        print(f"Updated record '{record_id}': {new_values}")
    return updated
