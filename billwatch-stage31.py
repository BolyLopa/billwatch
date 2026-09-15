# === Stage 31: Add compact table rendering for long lists ===
# Project: BillWatch
def render_compact_table(bills):
    """Render a compact table for long bill lists."""
    if not bills:
        return "No bills to display."
    headers = ["Name", "Due Date", "Status", "Amount"]
    rows = [headers]
    for bill in bills:
        row = [bill["name"], bill["due_date"], bill["status"], bill["amount"]]
        rows.append(row)
    width = sum(len(h) for h in headers) + len(rows) * 2
    separator = "+" + "-".join("-" * (len(h) + 2) for h in headers) + "+"
    lines = [separator]
    for row in rows:
        line = "| " + " | ".join(f"{str(cell)[:len(h)]}" for h, cell in zip(headers, row)) + " |"
        lines.append(line)
    lines.append(separator)
    return "\n".join(lines)
