import sqlite3

# 1. Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect('database.db')

# 2. Create a cursor to execute SQL commands
cur = conn.cursor()

# 3. Create a table
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    gender TEXT NOT NULL,
    device TEXT NOT NULL
)
''')

# 4. Insert data into the table
cur.execute('INSERT INTO users (name, gender, device) VALUES (?, ?, ?)', ("Krishna", "male", "ios"))

# 5. Query data from the table
cur.execute('SELECT * FROM users')
all_rows = cur.fetchall()
for row in all_rows:
    print(row)

# 6. Query specific data from the table
cur.execute('SELECT * FROM users WHERE id = ?', (1,))
all_rows = cur.fetchall()
for row in all_rows:
    print(row)

# 7. Delete table
cur.execute('DROP TABLE IF EXISTS users')

# 8. Commit changes and close
conn.commit()
conn.close()