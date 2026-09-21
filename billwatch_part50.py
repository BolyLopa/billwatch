# === Stage 50: Add unit tests for import and export behavior ===
# Project: BillWatch
import unittest
from datetime import date, timedelta

from billwatch import Bill, BillWatch, BillCategory

class TestImportExport(unittest.TestCase):
    def setUp(self):
        self.watch = BillWatch()

    def test_import_json_roundtrip(self):
        bill = Bill("Electric", date(2024, 3, 15), date(2024, 3, 30), 120.00, BillCategory.UTILITIES, "paid")
        self.watch.import_bill(bill)
        data = self.watch.export_json()
        self.assertEqual(data["bills"][0]["name"], "Electric")
        self.assertEqual(data["bills"][0]["due_date"], "2024-03-30")
        self.assertEqual(data["bills"][0]["amount"], 120.0)

    def test_export_csv(self):
        bill = Bill("Water", date(2024, 2, 1), date(2024, 2, 28), 45.50, BillCategory.UTILITIES, "paid")
        self.watch.import_bill(bill)
        csv = self.watch.export_csv()
        lines = csv.strip().split('\n')
        self.assertEqual(len(lines), 2)
        self.assertIn("Water", lines[1])

    def test_export_html(self):
        bill = Bill("Internet", date(2024, 4, 1), date(2024, 4, 15), 60.00, BillCategory.UTILITIES, "pending")
        self.watch.import_bill(bill)
        html = self.watch.export_html()
        self.assertIn("Internet", html)
        self.assertIn("pending", html)

    def test_import_csv_roundtrip(self):
        csv_data = "name,due_date,amount,category,status\nElectric,2024-03-30,120.0,UTILITIES,paid"
        self.watch.import_csv(csv_data)
        self.assertEqual(len(self.watch.bills), 1)
        self.assertEqual(self.watch.bills[0].name, "Electric")
        self.assertEqual(self.watch.bills[0].amount, 120.0)

    def test_import_html_roundtrip(self):
        html_data = "<html><body><table><tr><td>Electric</td><td>2024-03-30</td><td>120.0</td><td>UTILITIES</td><td>paid</td></tr></table></body></html>"
        self.watch.import_html(html_data)
        self.assertEqual(len(self.watch.bills), 1)
        self.assertEqual(self.watch.bills[0].name, "Electric")

if __name__ == "__main__":
    unittest.main()
