# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: BillWatch
def dry_run_mode():
    """Toggle dry-run mode: all mutating commands log instead of executing."""
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    from billwatch import DB
    try:
        db = DB()
        dry = db.get_setting('dry_run')
        if dry is None:
            db.set_setting('dry_run', False)
            print("Dry-run mode: OFF")
        else:
            db.set_setting('dry_run', True)
            print("Dry-run mode: ON (all writes will be logged, not saved)")
    except Exception as e:
        print("Error toggling dry-run:", e)
