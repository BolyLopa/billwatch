# === Stage 11: Add JSON export for the current application state ===
# Project: BillWatch
def export_json(data):
    import json
    with open("billwatch_export.json", "w") as f:
        json.dump(data, f, indent=2)
