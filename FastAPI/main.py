from typing import Optional
from fastapi import FastAPI, Request
from fastapi.params import Header
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str = "John Doe"
    email: Optional[str] = None
    
@app.get("/")
def root():
    return "Hello"

@app.get("/items/{item_id}/{item_name}")
@app.get("/items/{item_id}")
def read_item(item_id: int, item_name: Optional[str] = None):
    return {"item_id": item_id, "item_name": item_name}

@app.get("/test")
def test(query: str, page: int):
    return {"query": query, "page": page}

@app.post("/user")
def create_user(user: User, x_auth_token: str= Header(...)):
    return {"User": user, "Headers": x_auth_token}

