# === Stage 22: Add favorite records and quick favorite listing ===
# Project: BillWatch
import json

def add_favorite(bills, bill_id):
    """Mark a bill as favorite."""
    for bill in bills:
        if bill['id'] == bill_id:
            bill['favorite'] = True
            return bills
    raise ValueError(f"Bill {bill_id} not found")

def list_favorites(bills):
    """Return only favorite bills."""
    return [b for b in bills if b.get('favorite', False)]

def set_favorites(bills, ids):
    """Set favorites for a list of IDs."""
    for bill in bills:
        bill['favorite'] = bill['id'] in ids
    return bills
