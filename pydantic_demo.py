#  Students management system using pydantic.

# def create_student(name: str, age: int, college: str):
#     if type(name) == str and type(age) == int and type(college) == str:
#      print(name)
#      print(age)
#      print(college)
#      print("Student created!")
#     else:
#         raise TypeError("Invalid type of input data.")
# create_student('Chirag', 20, 'Masai')


# def update_student(name: str, age: int, college: str):
#     if type(name) == str and type(age) == int and type(college) == str:
#      print(name)
#      print(age)
#      print(college)
#      print("Student updated!")
#     else:
#         raise TypeError("Invalid type of input data.")
# update_student('Chirag', 20, 'Masai')
#  by default all the fields are required in pydantic base model, if you want to make any field optional you can use the Optional type hint from the typing module. Here's an example of how to make the college field optional:
# pydentic is a data validation library in Python that allows you to define data models and validate input data against those models. Here's how you can use pydantic to create a student management system:
# Type validation in pydantic - validating the data types of attributes in a pydantic model. When you define a pydantic model, you can specify the expected data types for each attribute. Pydantic will automatically validate the input data against these types and raise a ValidationError if the data does not conform to the specified types.
# create an ideal model class using pydantic
# ** -> unpacking the dictionary and passing it as keyword arguments to the student class constructor
#  Field validation in pydantic - validating the values of attributes in a pydantic model. In addition to type validation, pydantic also allows you to define custom validation rules for your model fields. You can use the @validator decorator to create custom validation methods that will be called during the validation process. These methods can check for specific conditions, such as ensuring that a string is not empty or that a number falls within a certain range.
# Any URL
from pydantic import BaseModel, ValidationError, Field, EmailStr, field_validator

class Student(BaseModel):
    name: str = Field(max_length=50, description= "provide the name of the student")
    email: EmailStr = Field(description="provide valid email of the student", examples = ["abc@gamil.com"])
    age: int
    college: str
# This field validator is used to validate if email belongs to masai.com or not
#  list= [1, 2, 3, 4, 5] = list[-1] -> 5

@field_validator('email')
@classmethod
def email_validator(Cls, value):
    domain_name = value.split('@')[-1]
    
    if domain_name != "masai.com":
      raise ValueError("not a valid domain for email.")
    return value

@field_validator('college')
@classmethod
def transform_college_name_to_upper_case(Cls, value):
    return value.upper()

@field_validator('age', mode = "before")
@classmethod
def validate_age(Cls, value):
    if value < 0 and value > 100:
     raise ValueError("Invalid age provided.")
    
    return value    
#  default value for mode is after

Student_info = {'name': 'Chirag', 'email': 'abc@google.com', 'age': '20', 'college': 'Masai'}

Student = Student(**Student_info)
print(Student.college) 

