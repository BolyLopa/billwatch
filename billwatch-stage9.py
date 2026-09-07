# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: BillWatch
def sort_bills(bills, key="title", reverse=False):
    """Sort bills by the given key attribute."""
    return sorted(bills, key=lambda b: b.get(key, ""), reverse=reverse)
