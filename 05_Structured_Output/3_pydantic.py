from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name: str = "Anjali Gupta"
    age: Optional[int] = None
    email: EmailStr

    # cgpa should be greater than 0 and less than 10
    cgpa: float = Field(
        gt=0,
        lt=10,
        default=5,
        description="Decimal value representing the marks of the students",
    )


# new_student = {"name": "Anjali Gupta"}
new_student = {"age": 21, "email": "abc@gmail.com"}

student = Student(**new_student)

student_dict = dict(student)
# print(student_dict["age"])

student_json = student.model_dump_json()
print(student_json)

# print(student.name)
# print(student)
