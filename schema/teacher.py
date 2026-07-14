from pydantic import BaseModel


class Teacher(BaseModel):
    name: str
    email: str
    course: str
    teacher_id: int