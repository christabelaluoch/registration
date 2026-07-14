from database import get_connection

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