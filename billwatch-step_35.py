# === Stage 35: Add active user switching and user-specific records ===
# Project: BillWatch
# Step 35: Add user switching and user-specific records
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<User {self.name}>"

class BillTracker:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def add_user(self, name):
        if name not in self.users:
            self.users[name] = User(name)
        return self.users[name]

    def switch_user(self, name):
        user = self.add_user(name)
        self.current_user = user
        return user

    def get_current_user(self):
        return self.current_user

    def add_bill(self, name, amount, due_date, category="Other", user=None):
        if self.current_user is None:
            self.switch_user("default")
        else:
            user = self.current_user
        bill = Bill(name, amount, due_date, category, user)
        user.bills.append(bill)
        return bill

    def get_user_bills(self, user=None):
        if user is None:
            user = self.current_user
        return user.bills

    def get_monthly_summary(self, year, month, user=None):
        if user is None:
            user = self.current_user
        bills = self.get_user_bills(user)
        total = sum(b.amount for b in bills if b.due_date.year == year and b.due_date.month == month)
        return {"year": year, "month": month, "total": total, "count": len(bills)}

    def set_status(self, name, status, user=None):
        if self.current_user is None:
            self.switch_user("default")
        else:
            user = self.current_user
        for bill in user.bills:
            if bill.name == name:
                bill.status = status
                return bill
        raise ValueError(f"No bill found with name: {name}")
