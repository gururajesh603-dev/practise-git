import sqlite3
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()
# CREATE
cursor.execute(
    "INSERT INTO expenses (title, amount, category) VALUES (?, ?, ?)",
    ("Lunch", 200, "Food")
)
# READ
cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()
print("Expenses:")
for row in rows:
    print(row)
# UPDATE
cursor.execute(
    "UPDATE expenses SET amount = ? WHERE id = ?",
    (250, 1)
)
# DELETE
cursor.execute(
    "DELETE FROM expenses WHERE id = ?",
    (2,)
)
conn.commit()
conn.close()