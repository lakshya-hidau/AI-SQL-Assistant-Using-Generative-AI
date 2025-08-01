import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)