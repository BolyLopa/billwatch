# === Stage 56: Add compact error classes for domain failures ===
# Project: BillWatch
class BillWatchError(Exception):
    """Base exception for all BillWatch domain failures."""
    pass


class BillNotFoundError(BillWatchError):
    """Raised when a bill with the given identifier is not found."""
    def __init__(self, bill_id):
        self.bill_id = bill_id
        super().__init__(f"Bill with id '{bill_id}' not found")


class BillAlreadyPaidError(BillWatchError):
    """Raised when attempting to mark a bill as paid that is already paid."""
    def __init__(self, bill_id):
        self.bill_id = bill_id
        super().__init__(f"Bill '{bill_id}' is already marked as paid")


class BillOverdueError(BillWatchError):
    """Raised when a bill is past its due date and still unpaid."""
    def __init__(self, bill_id, due_date):
        self.bill_id = bill_id
        self.due_date = due_date
        super().__init__(f"Bill '{bill_id}' is overdue (due: {due_date})")


class InvalidDateError(BillWatchError):
    """Raised when a date string cannot be parsed or is invalid."""
    def __init__(self, date_str):
        self.date_str = date_str
        super().__init__(f"Invalid date: '{date_str}'")


class InvalidCategoryError(BillWatchError):
    """Raised when a category name is empty, None, or not a string."""
    def __init__(self, category):
        self.category = category
        super().__init__(f"Invalid category: {category!r}")


class DuplicateBillError(BillWatchError):
    """Raised when a bill with an existing identifier is added."""
    def __init__(self, bill_id):
        self.bill_id = bill_id
        super().__init__(f"Bill with id '{bill_id}' already exists")
