# === Stage 83: Add regression tests for the final demo workflow ===
# Project: BillWatch
import pytest
from billwatch.core import Bill, BillTracker

def test_end_to_end_demo_workflow():
    tracker = BillTracker()
    tracker.add_bill(Bill("Electricity", "2024-05-15", "paid", "Utilities"))
    tracker.add_bill(Bill("Internet", "2024-05-20", "pending", "Utilities"))
    tracker.add_bill(Bill("Rent", "2024-05-01", "overdue", "Housing"))
    assert len(tracker.bills) == 3
    assert tracker.get_status_counts() == {"paid": 1, "pending": 1, "overdue": 1}
    assert tracker.get_category_total("Utilities") == 2
    assert tracker.is_overdue("Rent") is True
    assert tracker.is_overdue("Electricity") is False
    assert len(tracker.get_due_in("2024-05")) == 3

def test_demo_summary_report():
    tracker = BillTracker()
    tracker.add_bill(Bill("Electricity", "2024-05-15", "paid", "Utilities"))
    tracker.add_bill(Bill("Rent", "2024-05-01", "overdue", "Housing"))
    tracker.add_bill(Bill("Water", "2024-06-10", "pending", "Utilities"))
    report = tracker.generate_report()
    assert "May 2024" in report
    assert "Utilities" in report
    assert "Housing" in report
    assert "Total bills" in report
    assert "Paid" in report
    assert "Pending" in report
    assert "Overdue" in report
