# === Stage 14: Add file load support with fallback demo data ===
# Project: BillWatch
def load_data(path=None):
    if path and os.path.exists(path):
        import json
        with open(path) as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return data.get("bills", data.get("items", []))
    return DEMO_DATA
