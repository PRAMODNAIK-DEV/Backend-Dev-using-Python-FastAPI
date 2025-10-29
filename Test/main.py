
from pydantic import BaseModel

class Person(BaseModel):
    id: int
    name: str = "John Doe"
    email: str = None
    

p = Person(id="1", email="123", name="Alice")
print(p)


def add(a: int, b: int) -> int:
    return a + b