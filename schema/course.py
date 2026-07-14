from pydantic import BaseModel

class Course(BaseModel):
    name: str
    teacher_name: str
    course_id: str