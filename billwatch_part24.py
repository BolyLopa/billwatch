# === Stage 24: Add grouped summaries by category or status ===
# Project: BillWatch
def grouped_summary(bills, group_by='category'):
    """Return a dict with counts and total amounts grouped by category or status."""
    groups = {}
    for bill in bills:
        key = bill.get(group_by, 'other')
        if key not in groups:
            groups[key] = {'count': 0, 'total': 0.0}
        groups[key]['count'] += 1
        groups[key]['total'] += bill.get('amount', 0)
    return groups
