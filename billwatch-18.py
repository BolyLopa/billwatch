# === Stage 18: Add an activity log with timestamps and action names ===
# Project: BillWatch
class ActivityLog:
    def __init__(self):
        self.entries = []

    def add(self, action, user="system"):
        self.entries.append({"action": action, "user": user, "timestamp": datetime.now().isoformat()})

    def get(self):
        return self.entries
