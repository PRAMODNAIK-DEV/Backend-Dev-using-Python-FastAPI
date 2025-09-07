from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory "database"
items = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/items/")
def create_item(item: dict):
    items.append(item)
    return {"message": "Item created", "item": item}

@app.get("/items/")
def read_items():
    return {"items": items}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}

@app.put("/items/{item_id}")
def update_item(item_id: int, new_item: dict):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = new_item
    return {"message": "Item updated", "item": new_item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    removed_item = items.pop(item_id)
    return {"message": "Item deleted", "item": removed_item}