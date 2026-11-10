# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: BillWatch
def seed_demo_data(bills):
    if bills:
        return
    categories = {
        'Electric': 'Utilities',
        'Water': 'Utilities',
        'Internet': 'Communications',
        'Rent': 'Housing',
        'Groceries': 'Food',
        'Phone': 'Communications',
        'Gas': 'Utilities',
        'Insurance': 'Finance',
    }
    from datetime import date, timedelta
    today = date.today()
    sample = [
        ('Electric', 120.50, 'Paid', '2024-06-15', 30),
        ('Water', 45.00, 'Due', '2024-06-20', 30),
        ('Internet', 60.00, 'Paid', '2024-06-01', 30),
        ('Rent', 1200.00, 'Paid', '2024-06-01', 1),
        ('Groceries', 85.75, 'Paid', '2024-06-10', 28),
        ('Phone', 55.00, 'Overdue', '2024-06-05', 30),
        ('Gas', 70.25, 'Due', '2024-06-25', 30),
        ('Insurance', 200.00, 'Paid', '2024-06-15', 30),
    ]
    for name, amount, status, due_str, days in sample:
        due = today - timedelta(days=days)
        try:
            due = date.fromisoformat(due_str)
        except ValueError:
            pass
        bills.append({
            'name': name,
            'amount': amount,
            'status': status,
            'due_date': due,
            'category': categories.get(name, 'Other'),
        })
    print("Demo data seeded: 8 sample bills loaded.")
