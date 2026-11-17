# === Stage 87: Add small helper functions for comparing two exported reports ===
# Project: BillWatch
def normalize_report(report):
    normalized = []
    for entry in report:
        normalized.append({
            'bill': entry.get('bill'),
            'due_date': entry.get('due_date'),
            'status': entry.get('status'),
            'amount': entry.get('amount'),
            'category': entry.get('category'),
            'month': entry.get('month'),
        })
    return normalized


def compare_bills(report_a, report_b):
    normalized_a = normalize_report(report_a)
    normalized_b = normalize_report(report_b)
    differences = []
    for entry_a in normalized_a:
        for entry_b in normalized_b:
            if entry_a['bill'] != entry_b['bill']:
                differences.append({
                    'bill': entry_a['bill'],
                    'status': entry_a['status'],
                    'amount': entry_a['amount'],
                })
    return differences


def compare_categories(report_a, report_b):
    categories_a = {}
    for entry in report_a:
        category = entry.get('category')
        categories_a.setdefault(category, []).append(entry.get('status'))
    categories_b = {}
    for entry in report_b:
        category = entry.get('category')
        categories_b.setdefault(category, []).append(entry.get('status'))
    category_differences = []
    for category in categories_a:
        if category not in categories_b or categories_a[category] != categories_b[category]:
            category_differences.append({
                'category': category,
                'report_a': categories_a[category],
                'report_b': categories_b[category],
            })
    return category_differences


def compare_due_dates(report_a, report_b):
    due_dates_a = {}
    for entry in report_a:
        due_date = entry.get('due_date')
        due_dates_a.setdefault(due_date, []).append(entry.get('bill'))
    due_dates_b = {}
    for entry in report_b:
        due_date = entry.get('due_date')
        due_dates_b.setdefault(due_date, []).append(entry.get('bill'))
    due_date_differences = []
    for due_date in due_dates_a:
        if due_date not in due_dates_b or due_dates_a[due_date] != due_dates_b[due_date]:
            due_date_differences.append({
                'due_date': due_date,
                'report_a': due_dates_a[due_date],
                'report_b': due_dates_b[due_date],
            })
    return due_date_differences
