# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: BillWatch
# Tag helpers: add/remove tags and tag-based summaries
def add_tag(bills, tag):
    """Add tag to all bills that match tag."""
    for bill in bills:
        if bill["tag"] == tag:
            bill["tagged"] = True
            print(f"Tagged '{bill['name']}' with '{tag}'.")

def remove_tag(bills, tag):
    """Remove tag from all bills that match tag."""
    for bill in bills:
        if bill["tagged"] and bill["tag"] == tag:
            bill["tagged"] = False
            print(f"Untagged '{bill['name']}' from '{tag}'.")

def tag_summary(bills, tag):
    """Print summary for bills with given tag."""
    tagged = [b for b in bills if b.get("tag") == tag]
    if not tagged:
        print(f"No bills with tag '{tag}'.")
        return
    total = sum(b["amount"] for b in tagged)
    print(f"\nTag '{tag}' Summary:")
    print(f"  Bills: {len(tagged)}")
    print(f"  Total: {total:.2f}")
    for b in tagged:
        print(f"  - {b['name']}: {b['amount']:.2f} (due: {b['due_date']})")
