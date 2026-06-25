from fastapi import FastAPI
from pydantic import BaseModel
from database import (
    add_course,
    add_student,
    add_teacher,
    create_table,
    delete_course,
    delete_student,
    delete_teacher,
    get_course,
    get_courses,
    get_student,
    get_students,
    get_teacher,
    get_teachers,
    update_course,
    update_student,
    update_teacher,
)

app = FastAPI()
create_table()

class Student(BaseModel):
    name: str
    age: int
    email: str
    country: str
    id_number: int


class Teacher(BaseModel):
    name: str
    email: str
    course: str
    teacher_id: int


class Course(BaseModel):
    name: str
    teacher_name: str
    course_id: str


@app.get("/")
def home():
    return {"message": "Welcome to my API server"}



@app.get("/students")
def list_students():
    students = get_students()
    return students


@app.post("/students")
def register_student(student: Student):
    add_student(
        student.name, student.age, student.email, student.country, student.id_number
    )
    return {"message": "student registered", "student": student}


@app.get("/student/{id}")
def student_detail(id: int):
    student = get_student(id)
    return student


@app.put("/student/{id}")
def edit_student(id: int, student: Student):
    update_student(
        id, student.name, student.age, student.email, student.country, student.id_number
    )
    return {"message": "student updated", "student": student}


@app.delete("/student/{id}")
def remove_student(id: int):
    delete_student(id)
    return {"message": "student deleted"}



@app.get("/teachers")
def list_teachers():
    return get_teachers()  # Fixed: Called directly without 'database.'


@app.post("/teachers")
def register_teacher(teacher: Teacher):
    add_teacher(teacher.name, teacher.email, teacher.course, teacher.teacher_id)
    return {"message": "Teacher registered successfully", "teacher": teacher}


@app.get("/teachers/{id}")
def teacher_detail(id: int):
    teacher = get_teacher(id)
    return teacher


@app.put("/teachers/{id}")
def replace_teacher(id: int, teacher: Teacher):  # Fixed: Swapped parameter order
    update_teacher(
        id, teacher.name, teacher.email, teacher.course, teacher.teacher_id
    )
    return {"message": "Teacher record updated successfully", "teacher": teacher}


@app.delete("/teachers/{id}")
def remove_teacher(id: int):
    delete_teacher(id)
    return {"message": "Teacher record deleted successfully"}


@app.get("/courses")
def list_courses():
    return get_courses()  # Fixed: Called directly without 'database.'


@app.post("/courses")
def register_courses(course: Course):
    add_course(course.name, course.teacher_name, course.course_id)
    return {"message": "Course registered successfully", "course": course}


@app.get("/courses/{id}")
def course_detail(id: int):
    course = get_course(id)
    return course


@app.put("/courses/{id}")
def replace_course(id: int, course: Course):  # Fixed: Swapped parameter order
    update_course(id, course.name, course.teacher_name, course.course_id)
    return {"message": "Course record updated successfully", "course": course}


@app.delete("/courses/{id}")
def remove_course(id: int):
    delete_course(id)
    return {"message": "Course record deleted successfully"}


