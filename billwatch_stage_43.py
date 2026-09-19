# === Stage 43: Add CSV import for the primary record type ===
# Project: BillWatch
def import_csv(filepath):
    """Load BillWatch records from a CSV file.
    Expected columns: name, due_date, amount, category, status
    Returns a list of dicts ready to be merged into the global record list."""
    records = []
    with open(filepath, 'r') as f:
        headers = f.readline().strip().split(',')
        for line in f:
            line = line.strip()
            if not line:
                continue
            values = line.split(',')
            rec = {}
            for i, h in enumerate(headers):
                rec[h.strip()] = values[i].strip()
            rec['due_date'] = rec['due_date'].replace('-', '/')
            rec['status'] = rec['status'].lower()
            records.append(rec)
    return records
