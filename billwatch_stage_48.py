# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: BillWatch
import datetime

def add_days(date, days):
    return date + datetime.timedelta(days=days)

def is_valid_date(d):
    return isinstance(d, datetime.date)

def parse_bill_entry(line):
    parts = line.strip().split(',')
    if len(parts) != 4:
        return None
    try:
        due = datetime.date.fromisoformat(parts[0])
        amount = float(parts[1])
        category = parts[2].strip()
        status = parts[3].strip()
        if amount <= 0 or category not in ('rent', 'utilities', 'insurance', 'loans', 'subscriptions', 'other'):
            return None
        if status not in ('paid', 'due', 'overdue'):
            return None
        return {'due': due, 'amount': amount, 'category': category, 'status': status}
    except (ValueError, TypeError):
        return None
