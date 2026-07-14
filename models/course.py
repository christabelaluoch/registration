from database import get_connection

def create_table():
    with get_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     teacher_name TEXT NOT NULL,
                     course_id TEXT NOT NULL
                     )''')