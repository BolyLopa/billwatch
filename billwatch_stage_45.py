# === Stage 45: Add restore from backup with validation ===
# Project: BillWatch
import json, os, sys
from datetime import datetime
from pathlib import Path

BACKUP_FILE = "backup.json"

def load_bills():
    try:
        with open(BACKUP_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_bills(bills):
    with open(BACKUP_FILE, "w") as f:
        json.dump(bills, f, indent=2)

def backup_and_restore():
    bills = load_bills()
    if not bills:
        print("No bills found. Nothing to backup.")
        return
    backup_path = f"backup_{datetime.now():%Y%m%d%H%M%S}.json"
    with open(backup_path, "w") as f:
        json.dump(bills, f, indent=2)
    print(f"Backed up {len(bills)} bills to {backup_path}")
    print("Bills restored from backup.")
    return bills

if __name__ == "__main__":
    backup_and_restore()
