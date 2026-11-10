# === Stage 72: Add Markdown report export ===
# Project: BillWatch
def export_report(path, bills, categories):
    lines = []
    lines.append("BillWatch Monthly Report")
    lines.append("=" * 40)
    lines.append("")
    lines.append("SUMMARY")
    lines.append("-" * 40)
    total = sum(b["amount"] for b in bills)
    lines.append("Total amount: {:.2f}".format(total))
    lines.append("Paid: {:.2f}".format(sum(b["amount"] for b in bills if b["paid"])))
    lines.append("Overdue: {}".format(sum(1 for b in bills if not b["paid"] and b["due"] < "2000-01-01")))
    lines.append("")
    lines.append("CATEGORIES")
    lines.append("-" * 40)
    for name, data in categories.items():
        lines.append("{name}: {count} bills, {total:.2f}".format(name=name, count=data["count"], total=data["total"]))
    lines.append("")
    lines.append("BILLS")
    lines.append("-" * 40)
    for b in bills:
        lines.append("{category} | {amount:.2f} | {status} | {due}".format(
            category=b["category"], amount=b["amount"], status=b["status"], due=b["due"]))
    report = "\n".join(lines)
    with open(path, "w") as f:
        f.write(report)
    return report
