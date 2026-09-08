# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: BillWatch
import json

def load_bills(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("Top-level JSON must be a list of bills.")
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Malformed JSON in '{file_path}': {e}")
        return []
    except Exception as e:
        print(f"Unexpected error reading '{file_path}': {e}")
        return []
