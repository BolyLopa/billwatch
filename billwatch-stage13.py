# === Stage 13: Add file save support using a configurable path ===
# Project: BillWatch
import os
from datetime import datetime

SAVE_DIR = os.getenv("BILLWATCH_DIR", os.path.join(os.path.expanduser("~"), ".billwatch"))
SAVE_DIR = os.path.abspath(SAVE_DIR)
os.makedirs(SAVE_DIR, exist_ok=True)

class SaveManager:
    """Configurable file save support for BillWatch."""
    def __init__(self, path=None):
        self._path = path if path else os.path.join(SAVE_DIR, "bills.json")

    def _ensure_dir(self):
        d = os.path.dirname(self._path)
        os.makedirs(d, exist_ok=True)

    def save(self, data):
        self._ensure_dir()
        with open(self._path, "w") as f:
            import json
            json.dump(data, f, indent=2, default=str)
        return self._path

    def load(self):
        if not os.path.isfile(self._path):
            return []
        with open(self._path) as f:
            return json.load(f)
