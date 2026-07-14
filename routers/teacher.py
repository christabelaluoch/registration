from fastapi import APIRouter
from schema.teacher import Teacher
from repositories.teacher import(
    get_teacher,
    get_teachers,
    update_teacher,
    delete_teacher,
    add_teacher
    

)
router = APIRouter(prefix="/teacher",tags=["teachers"])
@router.get("/teachers")
def list_teachers():
    return get_teachers()  


@router.post("")
def register_teacher(teacher: Teacher):
    add_teacher(teacher.name, teacher.email, teacher.course, teacher.teacher_id)
    return {"message": "Teacher registered successfully", "teacher": teacher}


@router.get("{teacher_id}")
def teacher_detail(id: int):
    teacher = get_teacher(id)
    return teacher


@router.put("/{teachers_id}")
def replace_teacher(id: int, teacher: Teacher):  
    update_teacher(
        id, teacher.name, teacher.email, teacher.course, teacher.teacher_id
    )
    return {"message": "Teacher record updated successfully", "teacher": teacher}


@router.delete("{teachers_id}")
def remove_teacher(id: int):
    delete_teacher(id)
    return {"message": "Teacher record deleted successfully"}