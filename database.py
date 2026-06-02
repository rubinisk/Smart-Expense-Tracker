import sqlite3

def connect_db():
    return sqlite3.connect("expenses.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_expense(date, category, amount, description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses (date, category, amount, description)
    VALUES (?, ?, ?, ?)
    """, (date, category, amount, description))

    conn.commit()
    conn.close()

def get_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, date, category, amount, description FROM expenses ORDER BY date DESC")
    expenses = cursor.fetchall()

    conn.close()
    return expenses

def delete_expense(expense_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (expense_id,)
    )

    rows_deleted = cursor.rowcount

    conn.commit()
    conn.close()

    return rows_deleted

def get_total_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    conn.close()
    return total if total else 0

def update_expense(expense_id, date, category, amount, description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE expenses
        SET date=?, category=?, amount=?, description=?
        WHERE id=?
    """, (date, category, amount, description, expense_id))

    conn.commit()
    conn.close()

def get_category_summary():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    data = cursor.fetchall()

    conn.close()
    return data

def expense_exists(expense_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM expenses WHERE id=?",
        (expense_id,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None

if __name__ == "__main__":
    create_table()