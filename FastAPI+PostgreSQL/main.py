# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db import Base, engine, SessionLocal
from models import Item

# Create all database tables if it is not already present in the Database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.get("/")
def root():
    return {"data": "Welcome to FastAPI + PostgreSQL"}

@app.post("/items/")
def create_item(
    name: str, 
    description: str, 
    test_id: int,
    db: Session = Depends(get_db)
):
    new_item = Item(name=name, description=description, test_id=test_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"message": "Item created successfully", "item": new_item}

@app.get("/items/")
def get_all_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return {"items": items}

@app.get("/items/{item_id}")
def get_one_item(
    item_id: int, 
    db: Session = Depends(get_db)
):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        return {"item": item}
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str = None, description: str = None, test_id: int = None, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if name:
        item.name = name
    if description:
        item.description = description
    if test_id:
        item.test_id = test_id

    db.commit()
    db.refresh(item)
    return {"message": "Item updated successfully", "item": item}


@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}


# Example: SELECT * FROM items WHERE id=item_id AND test_id=2;
@app.get("/items/filter/")
def filter_items(item_id: int, test_id: int, db: Session = Depends(get_db)):
    
    items = db.query(Item).filter(
        Item.id == item_id,
        Item.test_id == test_id
    ).all()

    if not items:
        raise HTTPException(status_code=404, detail="No matching items found")
    
    return {"filtered_items": items}