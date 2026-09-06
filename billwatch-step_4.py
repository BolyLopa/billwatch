# === Stage 4: Implement create operations for the primary records ===
# Project: BillWatch
def create_bill(bills_db, bill_id, title, amount, due_date, category, status, notes=""):
    bill = {
        "id": bill_id,
        "title": title,
        "amount": amount,
        "due_date": due_date,
        "category": category,
        "status": status,
        "notes": notes,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    bills_db.append(bill)
    return bill
