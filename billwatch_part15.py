# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: BillWatch
def dispatch(text):
    """Convert a user text command into an action tuple."""
    t = text.strip().lower()
    if t.startswith("add "):
        return ("add", t[4:])
    if t.startswith("pay "):
        return ("pay", t[4:])
    if t.startswith("mark "):
        return ("mark", t[5:])
    if t.startswith("show "):
        return ("show", t[5:])
    if t.startswith("summary "):
        return ("summary", t[8:])
    if t.startswith("help"):
        return ("help", "")
    return None
