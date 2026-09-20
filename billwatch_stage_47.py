# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: BillWatch
def run_demo_scenarios():
    """Demonstrate the main workflow: add bills, mark payments, and view monthly summary."""
    bills = []
    bills.append(Bill(id=1, name="Electricity", amount=120.00, due_date="2024-01-15", category="Utilities"))
    bills.append(Bill(id=2, name="Internet", amount=79.99, due_date="2024-01-20", category="Utilities"))
    bills.append(Bill(id=3, name="Groceries", amount=250.00, due_date="2024-01-05", category="Food"))
    bills.append(Bill(id=4, name="Rent", amount=1500.00, due_date="2024-01-01", category="Housing"))

    bills.append(Bill(id=5, name="Water", amount=45.00, due_date="2024-02-10", category="Utilities"))
    bills.append(Bill(id=6, name="Phone Bill", amount=60.00, due_date="2024-02-15", category="Utilities"))

    bills.append(Bill(id=7, name="Groceries", amount=300.00, due_date="2024-02-05", category="Food"))
    bills.append(Bill(id=8, name="Rent", amount=1500.00, due_date="2024-02-01", category="Housing"))

    bills.append(Bill(id=9, name="Electricity", amount=130.00, due_date="2024-03-15", category="Utilities"))
    bills.append(Bill(id=10, name="Internet", amount=79.99, due_date="2024-03-20", category="Utilities"))
    bills.append(Bill(id=11, name="Groceries", amount=280.00, due_date="2024-03-05", category="Food"))

    for bill in bills:
        print(f"Bill: {bill.name}, Amount: ${bill.amount:.2f}, Due: {bill.due_date}, Category: {bill.category}")

    print("\nMonthly Summary:")
    monthly_total = 0
    for bill in bills:
        month = bill.due_date[:7]
        monthly_total += bill.amount
        print(f"Month: {month}, Total: ${monthly_total:.2f}")

    print("\nTotal Bills:", len(bills))
    print("Total Amount: $", sum(bill.amount for bill in bills))

run_demo_scenarios()
