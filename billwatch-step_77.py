# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: BillWatch
def is_overdue(due_date: date, today: date = None) -> bool:
    today = today or date.today()
    return due_date < today


def is_due_today(due_date: date, today: date = None) -> bool:
    today = today or date.today()
    return due_date == today


def days_until_due(due_date: date, today: date = None) -> int:
    today = today or date.today()
    return (due_date - today).days


def is_paid(bill: Bill) -> bool:
    return bill.status == "paid"


def get_due_bills(bills: List[Bill], today: date = None) -> List[Bill]:
    today = today or date.today()
    return [b for b in bills if b.status == "unpaid" and is_due_today(b.due_date, today)]


def get_overdue_bills(bills: List[Bill], today: date = None) -> List[Bill]:
    today = today or date.today()
    return [b for b in bills if b.status == "unpaid" and is_overdue(b.due_date, today)]


def get_monthly_bills(bills: List[Bill], month: int, year: int) -> List[Bill]:
    return [b for b in bills if b.due_date.month == month and b.due_date.year == year]


def get_bills_by_category(bills: List[Bill], category: str) -> List[Bill]:
    return [b for b in bills if b.category == category]


def get_monthly_summary(bills: List[Bill], month: int, year: int) -> dict:
    month_bills = get_monthly_bills(bills, month, year)
    total = sum(b.amount for b in month_bills)
    paid = [b for b in month_bills if is_paid(b)]
    unpaid = [b for b in month_bills if not is_paid(b)]
    return {
        "month": month,
        "year": year,
        "total": total,
        "paid_count": len(paid),
        "unpaid_count": len(unpaid),
        "total_paid": sum(b.amount for b in paid),
        "total_unpaid": sum(b.amount for b in unpaid),
    }


def get_category_summary(bills: List[Bill], month: int, year: int) -> dict:
    result: dict = {}
    for category in [b.category for b in bills]:
        result[category] = {
            "bills": 0,
            "amount": 0,
            "paid": 0,
            "unpaid": 0,
        }
    for bill in bills:
        if bill.due_date.month == month and bill.due_date.year == year:
            entry = result[bill.category]
            entry["bills"] += 1
            entry["amount"] += bill.amount
            if is_paid(bill):
                entry["paid"] += 1
            else:
                entry["unpaid"] += 1
    return result
