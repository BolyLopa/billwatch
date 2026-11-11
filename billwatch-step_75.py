# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: BillWatch
def generate_validation_report(bills):
    warnings = []
    errors = []
    valid_categories = {"electricity", "water", "internet", "phone", "gas", "rent", "insurance", "credit_card"}
    for bill in bills:
        if not isinstance(bill, dict):
            errors.append("Each bill entry must be a dictionary")
            continue
        required = ["title", "due_date", "amount", "status", "category"]
        for field in required:
            if field not in bill:
                errors.append("Missing field '%s' in bill for '%s'" % (field, bill.get("title", "unknown")))
        if "title" in bill and not bill["title"].strip():
            errors.append("Empty bill title in entry")
        if "amount" in bill:
            try:
                amount = float(bill["amount"])
                if amount <= 0:
                    errors.append("Invalid amount '%s' for bill '%s'" % (bill["amount"], bill.get("title", "unknown")))
            except (TypeError, ValueError):
                errors.append("Invalid amount type '%s' for bill '%s'" % (bill.get("amount"), bill.get("title", "unknown")))
        if "due_date" in bill:
            try:
                due = bill["due_date"]
                if isinstance(due, str):
                    datetime.datetime.strptime(due, "%Y-%m-%d")
            except (TypeError, ValueError, AttributeError):
                errors.append("Invalid due_date format '%s' for bill '%s'" % (bill.get("due_date"), bill.get("title", "unknown")))
        if "status" in bill:
            if bill["status"] not in ["paid", "unpaid", "overdue", "pending"]:
                warnings.append("Unknown status '%s' for bill '%s'" % (bill["status"], bill.get("title", "unknown")))
        if "category" in bill and bill["category"] not in valid_categories:
            warnings.append("Unknown category '%s' for bill '%s'" % (bill["category"], bill.get("title", "unknown")))
        if "due_date" in bill and "amount" in bill:
            try:
                due = bill["due_date"]
                if isinstance(due, str):
                    due_date = datetime.datetime.strptime(due, "%Y-%m-%d").date()
                else:
                    due_date = due
                today = datetime.date.today()
                if due_date < today and bill["status"] not in ["paid", "overdue"]:
                    warnings.append("Bill '%s' is past due and not marked overdue" % bill.get("title", "unknown"))
            except (TypeError, ValueError, AttributeError):
                warnings.append("Unable to check due date for bill '%s'" % bill.get("title", "unknown"))
    report = {"warnings": warnings, "errors": errors}
    return report
