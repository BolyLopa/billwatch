# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: BillWatch
def case_insensitive_search(self, query, field="name"):
    """Search across bill fields ignoring case, supporting partial matches."""
    query_lower = query.strip().lower()
    if not query_lower:
        return self.bills
    results = []
    for bill in self.bills:
        for attr in (field, "category", "due_date", "amount"):
            val = getattr(bill, attr, "")
            if query_lower in str(val).lower():
                results.append(bill)
                break
    return results
