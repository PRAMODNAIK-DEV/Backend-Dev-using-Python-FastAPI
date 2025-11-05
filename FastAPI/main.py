
from fastapi import FastAPI


app = FastAPI()


items = []

@app.get("/abc")
def root_endpoint():
    return {"message": "Hello, World!"}

# Endpoint or Path
@app.get("/items/")
def read_items():
    return {"items": items}
