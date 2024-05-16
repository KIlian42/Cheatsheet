import uvicorn
from fastapi import FastAPI, APIRouter, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    in_stock: bool

items_router = APIRouter()
users_router = APIRouter()

@items_router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": "Sample item", "description": "A sample item from items router"}
@items_router.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "description": item.description, "price": item.price, "in_stock": item.in_stock}

@users_router.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe"}
@users_router.post("/users/")
async def create_user(user: dict = Body(...)):
    return {"name": user.get("name"), "email": user.get("email")}

# Include the routers into the main app
app.include_router(items_router, prefix="/api")
app.include_router(users_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # uvicorn FastAPI.server:app --reload