# === Stage 51: Add unit tests for search and filter behavior ===
# Project: BillWatch
import unittest
from billwatch.tracker import Bill, Tracker

class TestSearchFilter(unittest.TestCase):
    def setUp(self):
        self.tracker = Tracker()
        self.tracker.add_bill(Bill("Electric", "2024-01-15", "paid", "utilities"))
        self.tracker.add_bill(Bill("Internet", "2024-02-10", "unpaid", "utilities"))
        self.tracker.add_bill(Bill("Rent", "2024-01-01", "paid", "housing"))

    def test_search_by_category(self):
        results = self.tracker.search(category="utilities")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].name, "Electric")
        self.assertEqual(results[1].name, "Internet")

    def test_search_by_due_date(self):
        results = self.tracker.search(due_date="2024-02-10")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Internet")

    def test_search_by_status(self):
        results = self.tracker.search(status="unpaid")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Internet")

    def test_search_combined_filters(self):
        results = self.tracker.search(category="utilities", status="unpaid")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Internet")

    def test_search_empty_result(self):
        results = self.tracker.search(category="groceries")
        self.assertEqual(len(results), 0)

    def test_search_due_date_range(self):
        results = self.tracker.search(due_date_range=("2024-01-01", "2024-01-31"))
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].name, "Electric")
        self.assertEqual(results[1].name, "Rent")

if __name__ == "__main__":
    unittest.main()
