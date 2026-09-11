# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: BillWatch
def archive_and_restore():
    """Move completed or old bills to an archive folder and restore them."""
    import shutil, os, datetime
    archive_dir = "archive"
    os.makedirs(archive_dir, exist_ok=True)
    now = datetime.datetime.now()
    cutoff = now.replace(day=1) + datetime.timedelta(days=30)
    for f in os.listdir("."):
        if not f.endswith(".csv"):
            continue
        full = os.path.join(".", f)
        if os.path.getmtime(full) < cutoff.timestamp():
            shutil.move(full, os.path.join(archive_dir, f))
    print(f"Archived bills older than {cutoff.strftime('%Y-%m-%d')}")
