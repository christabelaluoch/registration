from fastapi import APIRouter
from schema.course import Course
from repositories.course import(
    add_course,
    get_course,
    get_courses,
    update_course,
    delete_course,
)

router = APIRouter(prefix="/course",tags=["courses"])
@router.get("")
def list_courses():
    return get_courses()  


@router.post("")
def register_courses(course: Course):
    add_course(course.name, course.teacher_name, course.course_id)
    return {"message": "Course registered successfully", "course": course}


@router.get("/{course_id}")
def course_detail(id: int):
    course = get_course(id)
    return course


@router.put("/{courses_id}")
def replace_course(id: int, course: Course):  
    update_course(id, course.name, course.teacher_name, course.course_id)
    return {"message": "Course record updated successfully", "course": course}


@router.delete("/{course_id}")
def remove_course(id: int):
    delete_course(id)
    return {"message": "Course record deleted successfully"}