from fastapi import FastAPI, HTTPException
from app.models import Item
from app import crud

app = FastAPI()

@app.post("/items/")
def create(item: Item):
    return crud.create_item(item.dict())

@app.post("/items/bulk")
def create_bulk(items: list[Item]):
    return crud.create_items_bulk([i.dict() for i in items])

@app.get("/items/")
def read_all():
    return crud.get_all_items()

@app.get("/items/{item_id}")
def read(item_id: str):
    item = crud.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
def update(item_id: str, item: Item):
    return crud.update_item(item_id, item.dict())

@app.delete("/items/{item_id}")
def delete(item_id: str):
    deleted = crud.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"deleted": True}
