# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: BillWatch
def parse_date(date_str):
    """Parse a date string in common formats and return a date object.
    
    Supported formats: YYYY-MM-DD, DD/MM/YYYY, DD-MM-YYYY, YYYY/MM/DD.
    Returns None if the string cannot be parsed.
    """
    import datetime

    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%Y.%m.%d",
    ]

    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue

    raise ValueError(f"Unrecognized date format: '{date_str}'. "
                     f"Expected formats: YYYY-MM-DD, DD/MM/YYYY, DD-MM-YYYY, YYYY/MM/DD, YYYY.MM.DD")
