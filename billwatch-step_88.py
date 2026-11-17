# === Stage 88: Add safer defaults for empty input and missing optional fields ===
# Project: BillWatch
def safe_parse(value, default=None):
    try:
        if isinstance(value, str):
            value = value.strip()
        if value == "":
            return default
        return value
    except Exception:
        return default

def safe_int(value, default=0):
    try:
        if value is None or str(value).strip() == "":
            return default
        return int(float(str(value).strip().replace(",", "")))
    except (ValueError, TypeError):
        return default

def safe_float(value, default=0.0):
    try:
        if value is None or str(value).strip() == "":
            return default
        return float(str(value).strip().replace(",", ""))
    except (ValueError, TypeError):
        return default

def safe_date(value, default=None):
    if value is None or str(value).strip() == "":
        return default
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d", "%b %d, %Y", "%B %d, %Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return default

def safe_status(value, default="pending"):
    if value is None or str(value).strip() == "":
        return default
    return str(value).strip().lower()

def safe_category(value, default="Uncategorized"):
    if value is None or str(value).strip() == "":
        return default
    return str(value).strip()
