# FastAPI generates a "schema" with all your API using the OpenAPI standard for defining APIs.

"""POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data."""

from fastapi import FastAPI  # FastAPI is a Python class that provides all the functionality for your API.
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/users/me")
async def read_user():
    return {"user_id": "yash"}

@app.get("/users/{id}")
async def read_user(id: str):
    return {"user_id": id}

@app.get("/models/{model_name}")
async def get_model_name(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

########### Query Parameters ###########

fake_items_db = [{"item_name": "foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
#http://127.0.0.1:8000/items/?skip=0&limit=10

@app.get("/items/{item_id}")
async def read_item(item_id: str, needy: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "needy": needy}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"discription": "This is an amazing item that has a long description"})
    return item

########### Request Body ###########
class Item(BaseModel):
    name: str
    discription: str | None = None
    price: str
    tax: float | None = None

@app.post("/items/")
async def create_items(item: Item):
    return item
