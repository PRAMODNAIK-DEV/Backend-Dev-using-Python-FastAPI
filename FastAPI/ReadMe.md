# FastAPI Simple CRUD (Without Database)

This project demonstrates a simple CRUD (Create, Read, Update, Delete)
API using **FastAPI**, without any database.\
It uses an in-memory Python list as storage.

------------------------------------------------------------------------

## Setup Instructions

### 1. Create Virtual Environment

``` bash
python -m venv venv
```

### 2. Activate Virtual Environment

-   **Windows**

``` bash
.\venv\Scripts\activate
```


### 3. Install Dependencies

``` bash
pip install fastapi uvicorn
```

------------------------------------------------------------------------

## Code (main.py)

``` python
from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory "database"
items = []

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
```

------------------------------------------------------------------------

## Run the Application

``` bash
uvicorn main:app --reload
```

The API will be available at:

    http://127.0.0.1:8000

------------------------------------------------------------------------

## Test with Postman

### 1. **Create Item (POST)**

-   URL: `http://127.0.0.1:8000/items/`
-   Method: `POST`
-   Body (JSON):

``` json
{
  "name": "Book",
  "price": 100
}
```

### 2. **Get All Items (GET)**

-   URL: `http://127.0.0.1:8000/items/`
-   Method: `GET`

### 3. **Get Single Item (GET)**

-   URL: `http://127.0.0.1:8000/items/0`
-   Method: `GET`

### 4. **Update Item (PUT)**

-   URL: `http://127.0.0.1:8000/items/0`
-   Method: `PUT`
-   Body (JSON):

``` json
{
  "name": "Notebook",
  "price": 150
}
```

### 5. **Delete Item (DELETE)**

-   URL: `http://127.0.0.1:8000/items/0`
-   Method: `DELETE`