from fastapi import APIRouter
from schema.student import Student
from repositories.student import(
    add_student,
    get_students,
    get_student,
    update_student,
    delete_student,
)

router = APIRouter(prefix="/students",tags=["students"])

@router.get("")
def list_students():
    students = get_students()
    return students


@router.post("")
def register_student(student: Student):
    add_student(
        student.name, student.age, student.email, student.country, student.id_number
    )
    return {"message": "student registered", "student": student}


@router.get("/{student_id}")
def student_detail(id: int):
    student = get_student(id)
    return student


@router.put("/s{student_id}")
def edit_student(id: int, student: Student):
    update_student(
        id, student.name, student.age, student.email, student.country, student.id_number
    )
    return {"message": "student updated", "student": student}


@router.delete("/{student_id}")
def remove_student(id: int):
    delete_student(id)
    return {"message": "student deleted"}