# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: BillWatch
def filter_bills(self, status=None, category=None, owner=None, tag=None):
        """Filter bills by status, category, owner, or tag.

        Args:
            status: Filter by payment status ('paid', 'due', 'overdue').
            category: Filter by bill category (e.g., 'utilities', 'subscriptions').
            owner: Filter by owner name.
            tag: Filter by tag name.

        Returns:
            A list of bills matching all specified criteria.
        """
        filtered = list(self.bills)
        if status:
            filtered = [b for b in filtered if b.status == status]
        if category:
            filtered = [b for b in filtered if b.category == category]
        if owner:
            filtered = [b for b in filtered if b.owner == owner]
        if tag:
            filtered = [b for b in filtered if b.tag == tag]
        return filtered
