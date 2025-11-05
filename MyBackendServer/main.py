
from fastapi import FastAPI, Request
import json

from fastapi.params import Depends

app = FastAPI()


# ----------------------Middlewares ---------------------- #

@app.middleware("http")
async def first_middleware(request: Request, call_next):
    print("first_middleware")
    response = await call_next(request)
    print("first_middleware")
    
    return response

@app.middleware("http")
async def second_middleware(request: Request, call_next):
    print("second_middleware")
    response = await call_next(request)
    print("second_middleware")
    
    return response

# ---------------------Dependency Injection --------------------- #
def test(name: str | None = None, age: int | None = None):
    return {"name": name, "age": age}

def test2():
    return "This is a test-2 dependency"

# ----------------------Endpoints ---------------------- #
@app.get("/")
def read_root(
    result: str = Depends(test), 
    res2: str = Depends(test2)
):
    return {"First Dependency": result, "Second Dependency": res2}

@app.get("/search/{item_id}")
async def search_items(
    request: Request, 
    result: str = Depends(test)
):
    query_param = request.query_params
    body = await request.body()
    headers = request.headers
    path_param = request.path_params
    
    return {"query_param": query_param, 
            "body": json.loads(body), 
            "headers": headers, 
            "path_param": path_param,
            "result": result
        }


