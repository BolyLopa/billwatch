# === Stage 60: Add saved views for frequently used filters ===
# Project: BillWatch
class SavedView:
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}

    def __repr__(self):
        return f"SavedView(name={self.name!r}, filters={self.filters})"

class BillWatchApp:
    def __init__(self):
        self.bills = []
        self.saved_views = []

    def add_bill(self, bill):
        self.bills.append(bill)

    def view_saved(self):
        return [str(v) for v in self.saved_views]

    def save_view(self, name, filters):
        self.saved_views.append(SavedView(name, filters))
        return self.view_saved()

    def apply_saved(self, name):
        for v in self.saved_views:
            if v.name == name:
                return v.filters
        return None

    def get_monthly_summary(self):
        from datetime import datetime
        now = datetime.now()
        month = now.month
        year = now.year
        monthly = {}
        for b in self.bills:
            due = b.due_date
            if due.year == year and due.month == month:
                cat = b.category
                if cat not in monthly:
                    monthly[cat] = {"total": 0.0, "count": 0, "paid": 0.0}
                monthly[cat]["total"] += b.amount
                monthly[cat]["count"] += 1
                if b.paid:
                    monthly[cat]["paid"] += b.amount
        return monthly
