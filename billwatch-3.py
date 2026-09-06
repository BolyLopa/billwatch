# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: BillWatch
def validate_due_date(date_str):
    """Validate date string in YYYY-MM-DD format."""
    import datetime
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_positive_amount(amount):
    """Validate that amount is a positive number."""
    return isinstance(amount, (int, float)) and amount > 0

def validate_category(category):
    """Validate category against allowed values."""
    allowed = {"utilities", "rent", "insurance", "subscriptions", "loans", "medical", "education", "other"}
    return category in allowed

def validate_status(status):
    """Validate payment status."""
    allowed = {"pending", "paid", "overdue", "cancelled"}
    return status in allowed

def validate_short_text(text, max_length=50):
    """Validate short text fields like bill name."""
    return isinstance(text, str) and 1 <= len(text) <= max_length

def validate_identifier(identifier):
    """Validate unique bill identifier format."""
    return isinstance(identifier, str) and len(identifier) >= 3 and identifier.isalnum()
