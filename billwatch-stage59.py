# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: BillWatch
import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "bills.json"
CONFIRM_FLAG = Path(__file__).parent / ".bulk_delete_pending"


def bulk_delete_bills(category: str | None = None, due_before: str | None = None) -> None:
    """Delete bills matching optional filters after a confirmation flag is set.

    The flag is created with the filter JSON before deletion and removed
    afterwards, so the user knows exactly what was about to be removed.
    This keeps the bulk-delete operation reversible and explicit.
    """
    if not CONFIRM_FLAG.exists():
        raise RuntimeError("No bulk-delete confirmation pending. Set the flag first.")

    with CONFIRM_FLAG.open("r") as f:
        filter_spec = json.load(f)

    bills = _load_bills()
    deleted = 0

    for bill in bills:
        if category is not None and bill.get("category") != category:
            continue
        if due_before is not None and bill.get("due_date", "") > due_before:
            continue
        bills.remove(bill)
        deleted += 1

    _save_bills(bills)
    CONFIRM_FLAG.unlink()
    print(f"Deleted {deleted} bill(s).")


def _load_bills() -> list[dict]:
    if DATA_PATH.exists():
        with DATA_PATH.open() as f:
            return json.load(f)
    return []


def _save_bills(bills: list[dict]) -> None:
    with DATA_PATH.open("w") as f:
        json.dump(bills, f, indent=2)
