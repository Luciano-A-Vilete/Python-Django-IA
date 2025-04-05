from fastapi import FastAPI, HTTPException
from typing import Dict

app = FastAPI(
    title="Simple API",
    description="A basic API built with FastAPI for demonstration purposes.",
    version="1.0.0"
)

# Sample data stored in memory
items: Dict[int, dict] = {
    1: {"name": "Item One", "description": "This is item one."},
    2: {"name": "Item Two", "description": "This is item two."}
}

@app.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message.
    
    Returns:
        dict: A welcome message.
    """
    return {"message": "Welcome to the Simple API built with FastAPI!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Retrieve an item by its ID.
    
    Parameters:
        item_id (int): The ID of the item to retrieve.
    
    Returns:
        dict: The item details.
    
    Raises:
        HTTPException: If the item is not found.
    """
    if item_id in items:
        return items[item_id]
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/")
async def create_item(item: dict):
    """
    Create a new item.
    
    Parameters:
        item (dict): A dictionary containing the item's properties.
    
    Returns:
        dict: The newly created item with its assigned ID.
    """
    new_id = max(items.keys()) + 1 if items else 1
    items[new_id] = item
    return {"id": new_id, **item}

if __name__ == "__main__":
    import uvicorn
    # Run the API with hot-reload enabled for development
    uvicorn.run("api_app:app", host="127.0.0.1", port=8000, reload=True)
