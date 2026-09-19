# === Stage 44: Add backup creation for the data file ===
# Project: BillWatch
def create_backup(db_path):
    import shutil
    backup_path = db_path + ".backup"
    shutil.copy2(db_path, backup_path)
    return backup_path
