# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: BillWatch
def score_bills(bills, now, months):
    """Return a list of (bill, priority, message) tuples, highest priority first."""
    scored = []
    for b in bills:
        days = (b["due_date"] - now).days
        if b["paid"]:
            continue
        if days < 0:
            priority = "overdue"
            message = "overdue by {} days".format(-days)
        elif days <= 7:
            priority = "urgent"
            message = "due in {} days".format(days)
        elif days <= 30:
            priority = "soon"
            message = "due in {} days".format(days)
        else:
            priority = "later"
            message = "due in {} days".format(days)
        scored.append((b, priority, message))
    order = {"urgent": 0, "overdue": 1, "soon": 2, "later": 3}
    scored.sort(key=lambda item: order[item[1]])
    return scored

def recommend(bills, now):
    """Build a monthly summary with priority recommendations."""
    categories = {}
    for b in bills:
        cat = b.get("category", "other")
        categories.setdefault(cat, {"total": 0, "count": 0})
        if not b.get("paid"):
            categories[cat]["total"] += b.get("amount", 0)
            categories[cat]["count"] += 1
    summary = {
        "now": now,
        "categories": categories,
        "total_due": sum(c["total"] for c in categories.values()),
        "recommendations": score_bills(bills, now, months),
    }
    return summary
