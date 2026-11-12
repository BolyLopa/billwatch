# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: BillWatch
def parse_bill_line(line):
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    parts = [p.strip() for p in line.split(",")]
    if len(parts) < 6:
        return None
    name = parts[0]
    due = None
    try:
        due = datetime.date.fromisoformat(parts[1])
    except ValueError:
        due = None
    amount = None
    try:
        amount = float(parts[2])
    except ValueError:
        amount = None
    category = parts[3] if len(parts) > 3 else "Uncategorized"
    status = parts[4] if len(parts) > 4 else "pending"
    paid_on = None
    if len(parts) > 5 and parts[5]:
        try:
            paid_on = datetime.date.fromisoformat(parts[5])
        except ValueError:
            paid_on = None
    return Bill(name, due, amount, category, status, paid_on)


def load_bills(path):
    if not os.path.exists(path):
        return []
    bills = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            bill = parse_bill_line(line)
            if bill:
                bills.append(bill)
    return bills


def save_bills(bills, path):
    lines = ["# name, due (YYYY-MM-DD), amount, category, status, paid_on (YYYY-MM-DD)"]
    for bill in bills:
        due = bill.due.isoformat() if bill.due else ""
        paid = bill.paid_on.isoformat() if bill.paid_on else ""
        lines.append(f"{bill.name},{due},{bill.amount},{bill.category},{bill.status},{paid}")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def bills_in_month(bills, month):
    year, m = month
    return [b for b in bills if b.due and b.due.year == year and b.due.month == m]


def summary_for_month(bills, month):
    year, m = month
    month_bills = bills_in_month(bills, month)
    total = sum(b.amount for b in month_bills if b.amount is not None)
    pending = [b for b in month_bills if b.status != "paid"]
    overdue = [b for b in pending if b.due and b.due < datetime.date.today()]
    return {
        "year": year,
        "month": m,
        "total": total,
        "pending_count": len(pending),
        "overdue_count": len(overdue),
        "bills": month_bills,
    }
