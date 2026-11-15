# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: BillWatch
def prune_bills(bills):
    return [b for b in bills if b['paid']]

def summarize_month(bills, month, year):
    return {
        'month': month,
        'year': year,
        'total': sum(b['amount'] for b in bills if b['month'] == month and b['year'] == year),
        'paid': sum(1 for b in bills if b['paid']),
    }
