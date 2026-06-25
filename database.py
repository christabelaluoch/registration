import sqlite3
from contextlib import contextmanager

sqlite_file_name="school.db"

@contextmanager
def get_connection():
    connection=sqlite3.connect(sqlite_file_name)
    connection.row_factory=sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close() 

def create_table():
    with get_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS students(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     age INTEGER NOT NULL,
                     email TEXT NOT NULL,
                     country TEXT NOT NULl,
                     id_number INTEGER NOT NULL
                    )''')
        connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     email TEXT NOT NULL,
                     course TEXT NOT NULL,
                     teacher_id INTEGER NOT NULL
                    )''')
        
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     teacher_name TEXT NOT NULL,
                     course_id TEXT NOT NULL
                     )''')



def add_student(name,age,email,country,id_number):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO students (name,age,email,country,id_number) VALUES(?,?,?,?,?)',
            (name,age,email,country,id_number),
        ) 

def get_students():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM students').fetchall() 

def get_student(student_id):
    with get_connection() as connection:
        return connection.execute('SELECT * FROM students WHERE id=?', (student_id)).fetchone() 
    
def update_student(student_id, name, age, email, country, id_number):
    with get_connection() as connection:
        connection.execute(
            '''UPDATE students SET name=?,age=?,email=?,country=?,id_number=?
               WHERE id=?''',
            (name, age, email, country, id_number, student_id),
        )


def delete_student(student_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM students WHERE id=?', (student_id,))


def add_teacher(name, email, course, teacher_id):
    with get_connection() as connection:
         connection.execute('INSERT INTO teachers (name, email, course, teacher_id) VALUES (?,?,?,?)',
             (name, email, course, teacher_id)
        )

def get_teachers():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()

def get_teacher(teacher_id):
    with get_connection() as connection: 
        return connection.execute('SELECT * FROM teachers WHERE id = ?',(teacher_id,)).fetchone()

def update_teacher(id, name, email, course, teacher_id):
    with get_connection() as connection:
        connection.execute('UPDATE teachers SET name = ?, email = ?, course = ?, teacher_id = ? WHERE ID = ?',
                (name, email, course, teacher_id, id)
                )

def delete_teacher(id):
    with get_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE id = ?',(id,))

def add_course(name, teacher_name, course_id):
    with get_connection() as connection:
        connection.execute('INSERT INTO courses (name,teacher_name,course_id) VALUES (?,?,?)',
                 (name, teacher_name, course_id))

def get_courses():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()

def get_course(course_id):
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses WHERE id = ?',(course_id,)).fetchone()

def update_course(id, name, teacher_name, course_id):
    with get_connection() as connection:
        connection.execute('UPDATE courses SET name = ?, teacher_name = ?, course_id = ? WHERE id = ?',
                   (name, teacher_name, course_id, id))

def delete_course(id):
    with get_connection() as connection:
        connection.execute('DELETE FROM courses WHERE id = ?',(id,))