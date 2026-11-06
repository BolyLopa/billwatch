# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: BillWatch
def reset_demo_data(db_path="bills.db"):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS bills")
    cur.execute("CREATE TABLE bills (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, category TEXT, due_date TEXT, amount REAL, paid INTEGER DEFAULT 0)")
    cur.execute("DROP TABLE IF EXISTS categories")
    cur.execute("CREATE TABLE categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)")
    demo = [("Electricity", "utilities", "2025-02-15", 120.0),
            ("Water", "utilities", "2025-02-20", 45.5),
            ("Internet", "services", "2025-02-10", 59.99),
            ("Rent", "housing", "2025-02-01", 900.0),
            ("Groceries", "shopping", "2025-02-25", 150.0)]
    cats = [row[0] for row in demo]
    for name in cats:
        cur.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (name,))
    for name, cat, due, amount in demo:
        cur.execute("INSERT INTO bills (name, category, due_date, amount, paid) VALUES (?, ?, ?, ?, 0)", (name, cat, due, amount))
    conn.commit()
    print("Demo data reset complete.")
    conn.close()
