# === Stage 73: Add a lightweight HTML report export ===
# Project: BillWatch
def export_html_report(bills, months=None):
    if months is None:
        months = sorted(set(b["month"] for b in bills))
    lines = ['<!DOCTYPE html>', '<html><head><meta charset="utf-8">',
             '<title>BillWatch Report</title>',
             '<style>body{font-family:sans-serif}table{border-collapse:collapse}th,td{padding:6px 10px;border:1px solid #ccc}th{background:#f0f0f0}</style>',
             '</head><body><h1>BillWatch Report</h1>']
    lines += ['<h2>Monthly Summary</h2>', '<table><tr><th>Month</th><th>Total</th><th>Count</th></table>']
    for m in months:
        subset = [b for b in bills if b["month"] == m]
        total = sum(b["amount"] for b in subset)
        lines += ['<tr><td>%s</td><td>%s</td><td>%d</td></tr>' % (m, "%.2f" % total, len(subset))]
    lines += ['</table>', '<h2>All Bills</h2>', '<table><tr><th>Name</th><th>Category</th><th>Due</th><th>Amount</th><th>Status</th></tr>']
    for b in bills:
        lines.append('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
                     % (b["name"], b["category"], b["due"], "%.2f" % b["amount"], b["status"]))
    lines += ['</table>', '</body></html>']
    with open("billwatch_report.html", "w") as f:
        f.write("\n".join(lines))
    return "billwatch_report.html"
