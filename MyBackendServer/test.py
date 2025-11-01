from typing import Optional
from pydantic import BaseModel, Field, field_validator, model_validator, validator, conint

class Student(BaseModel):
    age: conint(gt=0, le=120)
    tags: conlist(str, min_items=1, max_items=5)
    
    
s1 = Student(age=20, tags=['math', 'science'])
print(s1)
