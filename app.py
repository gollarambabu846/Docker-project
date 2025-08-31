from flask import Flask, render_template_string, g
import sqlite3

app = Flask(__name__)
DATABASE = 'students.db'

# HTML template for rendering students table
TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Students Marks</title>
    <style>
        table {border-collapse: collapse; width: 50%; margin: 20px auto;}
        th, td {border: 1px solid #ddd; padding: 8px; text-align: center;}
        th {background-color: #4CAF50; color: white;}
    </style>
</head>
<body>
    <h2 style="text-align:center;">Students Marks and Percentage</h2>
    <table>
        <tr>
            <th>Name</th>
            <th>Class</th>
            <th>Marks Obtained</th>
            <th>Total Marks</th>
            <th>Percentage</th>
        </tr>
        {% for student in students %}
        <tr>
            <td>{{ student.name }}</td>
            <td>{{ student.student_class }}</td>
            <td>{{ student.marks }}</td>
            <td>{{ student.total_marks }}</td>
            <td>{{ "%.2f"|format(student.percentage) }}%</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
'''

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db:
        db.close()

@app.route('/')
def index():
    db = get_db()
    cursor = db.execute('SELECT name, student_class, marks, total_marks FROM students')
    students = []
    for row in cursor.fetchall():
        percentage = (row['marks'] / row['total_marks']) * 100
        students.append({
            'name': row['name'],
            'student_class': row['student_class'],
            'marks': row['marks'],
            'total_marks': row['total_marks'],
            'percentage': percentage
        })
    return render_template_string(TEMPLATE, students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
