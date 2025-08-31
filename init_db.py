import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    student_class TEXT NOT NULL,
    marks INTEGER NOT NULL,
    total_marks INTEGER NOT NULL
)
''')

students_data = [
    ('Alice', '1st Year', 450, 500),
    ('Bob', '1st Year', 380, 500),
    ('Charlie', '1st Year', 420, 500),
    ('Diana', '1st Year', 390, 500)
]

cursor.executemany('INSERT INTO students (name, student_class, marks, total_marks) VALUES (?, ?, ?, ?)', students_data)
conn.commit()
conn.close()

print("Database initialized and seeded!")
