# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: BillWatch
class BillTracker:
    def __init__(self):
        self.bills = []
        self.monthly_summary = {}

    def add_bill(self, name, due_date, category, amount, status='pending'):
        bill = {
            'name': name,
            'due_date': due_date,
            'category': category,
            'amount': amount,
            'status': status
        }
        self.bills.append(bill)
        self.monthly_summary[category] = self.monthly_summary.get(category, 0) + amount
        return bill

    def get_due_bills(self):
        return [bill for bill in self.bills if bill['status'] == 'pending']

    def get_paid_bills(self):
        return [bill for bill in self.bills if bill['status'] == 'paid']

    def get_overdue_bills(self):
        return [bill for bill in self.bills if bill['status'] == 'overdue']

    def get_total_bills(self):
        return sum(bill['amount'] for bill in self.bills)

    def get_monthly_summary(self):
        return self.monthly_summary

    def display_bills(self):
        print("\n=== BillTracker Dashboard ===")
        print("Pending bills:")
        for bill in self.get_due_bills():
            print(f"  - {bill['name']} (${bill['amount']:.2f}) due on {bill['due_date']}")
        print("\nPaid bills:")
        for bill in self.get_paid_bills():
            print(f"  - {bill['name']} (${bill['amount']:.2f}) paid on {bill['due_date']}")
        print("\nOverdue bills:")
        for bill in self.get_overdue_bills():
            print(f"  - {bill['name']} (${bill['amount']:.2f}) overdue since {bill['due_date']}")
        print(f"\nTotal bills: ${self.get_total_bills():.2f}")

    def display_monthly_summary(self):
        print("\nMonthly Summary:")
        for category, amount in self.get_monthly_summary().items():
            print(f"  - {category}: ${amount:.2f}")
