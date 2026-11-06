# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: BillWatch
def build_changelog(entries):
    """Generate a compact changelog from the activity log.

    Each entry is a dict with keys: date, author, action, file.
    Returns a markdown-formatted string grouped by date.
    """
    by_date = {}
    for entry in sorted(entries, key=lambda e: e.get("date", "")):
        by_date.setdefault(entry["date"], []).append(entry)

    lines = ["# Changelog", ""]
    for date in sorted(by_date, reverse=True):
        lines.append(f"## {date}")
        for entry in by_date[date]:
            lines.append(f"- **{entry['author']}** {entry['action']} {entry['file']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"
