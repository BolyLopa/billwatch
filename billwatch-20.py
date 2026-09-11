# === Stage 20: Add duplicate detection for newly created records ===
# Project: BillWatch
def duplicate_check(self, category, amount, due_date, payment_status, notes, monthly_summary):
        if not all([category, amount, due_date, payment_status, notes, monthly_summary]):
            return False
        for i in range(len(self.bills)):
            if self.bills[i].category == category and self.bills[i].amount == amount and self.bills[i].due_date == due_date and self.bills[i].payment_status == payment_status and self.bills[i].notes == notes and self.bills[i].monthly_summary == monthly_summary:
                return False
        return True
