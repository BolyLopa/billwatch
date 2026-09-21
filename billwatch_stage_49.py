# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: BillWatch
import unittest
from billwatch.models.bill import Bill
from billwatch.models.bill import BillStatus
from billwatch.models.bill import PaymentStatus
from billwatch.models.bill import BillCategory


class BillTest(unittest.TestCase):
    def setUp(self):
        self.bill1 = Bill("Electric", "Electric", due_date="2024-01-01", amount=100.0, status=BillStatus.DUE)
        self.bill2 = Bill("Water", "Water", due_date="2024-01-15", amount=50.0, status=BillStatus.DUE)

    def test_update_due_date_on_overdue_bill(self):
        self.bill1.update_due_date("2024-02-01")
        self.assertEqual(self.bill1.due_date, "2024-02-01")

    def test_update_status_on_paid_bill(self):
        self.bill1.update_status(PaymentStatus.PAID)
        self.assertEqual(self.bill1.status, PaymentStatus.PAID)

    def test_delete_overdue_bill(self):
        self.bill1.update_status(PaymentStatus.OVERDUE)
        self.bill2.update_status(PaymentStatus.PAID)
        self.bill3 = Bill("Gas", "Gas", due_date="2024-01-01", amount=80.0, status=BillStatus.DUE)
        self.bill3.update_status(PaymentStatus.PAID)
        result = Bill.delete_overdue_bills([self.bill1, self.bill2, self.bill3])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.bill2)

    def test_delete_non_overdue_bills(self):
        bills = [self.bill1, self.bill2]
        result = Bill.delete_overdue_bills(bills)
        self.assertEqual(len(result), 0)

    def test_delete_mixed_bills(self):
        self.bill1.update_status(PaymentStatus.PAID)
        bills = [self.bill1, self.bill2]
        result = Bill.delete_overdue_bills(bills)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.bill2)


if __name__ == "__main__":
    unittest.main()
