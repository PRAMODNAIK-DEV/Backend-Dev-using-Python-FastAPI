from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, Header, Request
from pydantic import BaseModel

app = FastAPI()


@app.middleware("http")
async def first_middleware(request: Request, call_next):
    print("first_middleware: Before request")
    response = await call_next(request)
    print("first_middleware: After request")
    return response

@app.middleware("http")
async def second_middleware(request: Request, call_next):
    print("second_middleware: Before request-2")
    response = await call_next(request)
    print("second_middleware: After request-2")
    return response


# In Memory Database
items = [{"id": 0, "name": "Item 0"}, {"id": 1, "name": "Item 1"}]

users = []
# Endpoint || Path || Route
# GET, POST, PUT, PATCH & DELETE
@app.get("/")
def read_root():
    return {"Hello": "World"}

def health_dependency(name: str | None = None, age: int | None = None):
    return {"service": "up", "name": name, "age": age}

def get_token_header(x_token: str = Header(...)):
    if x_token != "secure-token":
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    return x_token

def get_query_param(q: Optional[str] = None):
    return q

@app.get("/health")
def health_check(
    token: str = Depends(test_token),
    query: str = Depends(extract_query)
    ):
    return {"status": "healthy", "token": token, "query": query}


class Address(BaseModel):
    street: str
    city: str
    
class User(BaseModel):
    name: str
    age: int
    mobile: Optional[str] = None
    address: Address

@app.post("/users/")
def create_user(
    user_data: User, 
    request: Request,
    x_token: Optional[str] = Header(None)
):
    users.append(user_data)
    headers = dict(request.headers)
    return {"message": "User created successfully", "headers": headers['x-pramod']}


# x-token
# x_token



@app.get("/items/")
def get_items(item_id: int, name: str = None, age: int = None, test: int = None):
    if item_id and item_id >= 0 and item_id < len(items):
        return {"item": items[item_id], "name": name, "age": age, "test": test}
    raise HTTPException(status_code=404, detail="Item not found")


# select * from items where item_id=item_id and test_id=2 and sub_id='abc';

# @app.get("/items/")
# def get_items():
#     return {"items": items}

# @app.get("/items/{item_id}")
# def read_one_item(item_id: int):
#     # if 0 >= item_id < len(items):
#     if item_id >= 0 and item_id < len(items):
#         return {"item": items[item_id]}
#     raise HTTPException(status_code=404, detail="Item not found")

# @app.post("/items/")
# def create_item(new_item: dict):
#     items.append(new_item)
#     return {"message": "Item created successfully", "item": new_item}
    

# @app.put("/items/{item_id}")
# def replace_item(item_id: int, updated_data: dict):
#     if item_id >= 0 and item_id < len(items):
#         items[item_id] = updated_data
#         return {"message": "Item updated successfully", "item": items[item_id]}
#     raise HTTPException(status_code=404, detail="Item not found")

# @app.delete("/items/{item_id}")
# def remove_item(item_id: int):
#     if item_id>=0 and item_id <len(items):
#         deleted_item = items.pop(item_id)
#         return {"message": "Item deleted successfully", "item": deleted_item}
#     raise HTTPException(status_code=404, detail="Item not found")