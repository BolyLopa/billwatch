# === Stage 42: Add CSV export without external dependencies ===
# Project: BillWatch
def export_to_csv(bills, filename="bills.csv"):
    if not bills:
        return
    headers = ["id", "name", "category", "amount", "due_date", "status", "notes"]
    with open(filename, "w", newline="") as f:
        f.write(",".join(headers) + "\n")
        for b in bills:
            row = [
                b["id"],
                b["name"],
                b["category"],
                b["amount"],
                b["due_date"],
                b["status"],
                b.get("notes", ""),
            ]
            f.write(",".join(row) + "\n")
