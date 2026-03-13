import sqlite3
# connect to database
conn = sqlite3.connect("expenses.db")
# create cursor
cursor = conn.cursor()
# create table
cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,amount REAL,category TEXT)""")
print("Table created successfully")
# save changes
conn.commit()
# close connection
conn.close()