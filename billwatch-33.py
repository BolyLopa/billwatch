# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: BillWatch
# Step 33: Settings dictionary and update functions

SETTINGS = {
    "currency": "USD",
    "language": "en",
    "sort_by": "due_date",
    "sort_order": "asc",
    "default_category": "utilities",
    "notifications": False,
    "show_expired": True,
}

def get_setting(key):
    return SETTINGS.get(key)

def update_setting(key, value):
    if key in SETTINGS:
        SETTINGS[key] = value
        return True
    return False

def reset_settings():
    SETTINGS.update({
        "currency": "USD",
        "language": "en",
        "sort_by": "due_date",
        "sort_order": "asc",
        "default_category": "utilities",
        "notifications": False,
        "show_expired": True,
    })
