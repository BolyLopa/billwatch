# === Stage 46: Add a schema version field and migration helper ===
# Project: BillWatch
import json

SCHEMA_VERSION = 2

def migrate_bills(bills, target_version):
    if target_version == SCHEMA_VERSION and SCHEMA_VERSION > 1:
        migrated = []
        for bill in bills:
            record = {
                "id": bill["id"],
                "name": bill["name"],
                "due_date": bill["due_date"],
                "amount": bill["amount"],
                "category": bill["category"],
                "status": bill["status"],
                "paid_date": bill.get("paid_date"),
                "notes": bill.get("notes"),
                "schema_version": SCHEMA_VERSION,
            }
            migrated.append(record)
        return migrated
    return bills

def save_bills(bills, filepath):
    with open(filepath, "w") as f:
        json.dump(bills, f, indent=2)

def load_bills(filepath):
    with open(filepath, "r") as f:
        bills = json.load(f)
    if bills:
        bills = migrate_bills(bills, SCHEMA_VERSION)
    return bills
