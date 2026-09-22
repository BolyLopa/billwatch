# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: BillWatch
def get_due_soon(bills, days=7):
    """Return bills whose due date is within *days* days from today.

    A bill is considered 'due soon' if its due date is on or after today
    and within the given number of days.
    """
    today = datetime.date.today()
    return [b for b in bills if today <= b.due_date <= today + timedelta(days=days)]


def get_overdue(bills):
    """Return bills that are past their due date and not yet paid.

    These bills have a due date before today and a payment status of 'pending'.
    """
    today = datetime.date.today()
    return [b for b in bills if b.due_date < today and b.status == 'pending']


def get_monthly_summary(bills, month):
    """Return a summary of bills due in a specific month.

    The summary includes the total number of bills, the number of overdue
    bills, and the list of unique categories.
    """
    today = datetime.date.today()
    month_start = month.replace(day=1)
    month_end = (month_start + datetime.timedelta(days=31)).replace(day=1)
    month_bills = [b for b in bills if month_start <= b.due_date <= month_end]
    overdue = [b for b in month_bills if b.due_date < today and b.status == 'pending']
    categories = list(set(b.category for b in month_bills))
    return {
        'month': month,
        'total_bills': len(month_bills),
        'overdue_bills': len(overdue),
        'categories': categories,
    }


def get_payment_history(bills, category):
    """Return the payment history for a specific category.

    The history includes the total number of payments, the total amount paid,
    and the list of unique payment methods used.
    """
    paid_bills = [b for b in bills if b.status == 'paid']
    category_bills = [b for b in paid_bills if b.category == category]
    payment_methods = list(set(b.payment_method for b in category_bills))
    return {
        'category': category,
        'total_payments': len(category_bills),
        'total_amount': sum(b.amount for b in category_bills),
        'payment_methods': payment_methods,
    }
