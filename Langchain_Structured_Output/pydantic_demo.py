from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str='Sagar'       ### Default Value assignment
    age:Optional[int]=None   ### Optional Fields
    email:EmailStr        ### Email Validation
    cgpa:float=Field(gt=0,lt=10,default=5,description="A decimal value reprsenting the cgpa of the student")

#new_student={'name':"Sagar"}

#new_student={'age':31}

#new_student={'age':'31','email':'abc@gmail.com','cgpa':8}

new_student={'age':'31','email':'abc@gmail.com','cgpa':8}

student=Student(**new_student)

student_dict=dict(student)   ### converting pydantic object to dictionary object

student_json=student.model_dump_json()  ### converting pydantic object to json object.

print(student)

print(student.name)

print(type(student))

print(student_dict['age'])