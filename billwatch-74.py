# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: BillWatch
def snapshot_difference(bills, before=None):
    if before is None:
        before = [dict(b) for b in bills]
    diff = []
    for bill in bills:
        b = dict(before)
        b.pop(bill['id'], None)
        for key in ['due_date', 'status', 'category', 'amount']:
            if b.get(key) != bill.get(key):
                diff.append({'id': bill['id'], 'field': key, 'old': b.get(key), 'new': bill.get(key)})
    return diff


def snapshot_summary(bills, before=None):
    if before is None:
        before = [dict(b) for b in bills]
    after_total = sum(b['amount'] for b in bills if b['status'] == 'paid')
    before_total = sum(b['amount'] for b in before if b['status'] == 'paid')
    return {'paid_before': before_total, 'paid_after': after_total, 'change': after_total - before_total}


def snapshot_comparison(bills, before=None):
    return {'changed': snapshot_difference(bills, before), 'summary': snapshot_summary(bills, before)}
