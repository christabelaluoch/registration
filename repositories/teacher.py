from database import get_connection


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
        