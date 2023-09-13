# FastAPI generates a "schema" with all your API using the OpenAPI standard for defining APIs.

"""POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data."""
# =========> Main Code <=========
from fastapi import FastAPI, Query, Path  # FastAPI is a Python class that provides all the functionality for your API.
from enum import Enum
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()
# ======================================================

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello world"}
#
#
# @app.get("/users/me")
# async def read_user():
#     return {"user_id": "yash"}
#
#
# @app.get("/users/{id}")
# async def read_user(identity_no: str):
#     return {"user_id": identity_no}
#
#
# @app.get("/models/{model_name}")
# async def get_model_name(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}
#
#
# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}


# =========> Query Parameters <=========

# fake_items_db = [{"item_name": "foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
#
# @app.get("/items/")
# async def read_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]
#
#
# http://127.0.0.1:8000/items/?skip=0&limit=10
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, needy: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "needy": needy}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
#     return item


# =========> Request Body <=========
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# @app.post("/model_items/")
# async def create_items(item: Item):
#     item_dict = item.model_dump()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
#
#
# @app.put('/model_items/{item_id}')
# async def create_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.model_dump()}
#     if q:
#         result.update({"q": q})
#     return result

# ===========> Query Parameters and String Validations <===========
# @app.get("/items")
# async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedPattern$")] = "Hi I am fixed :("):
# async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedPattern")] = ...): #Here q is required but also can take value of None
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
#
# @app.get("/items/list")
# async def read_items(q: Annotated[list[str] | None, Query(
#     alais="list-query",
#     title="Query String",
#     description="A very long description",
#     min_length=3,
#     include_in_schema= False
# )] = None):
#     query_items = {"q": q}
#     return query_items


# @app.get("/items/list")
# async def read_items(q: Annotated[list[str] | None, Query()] = ["None", "Hello"]):
#     query_items = {"q": q}
#     return query_items


# @app.get("/items/list")
# async def read_items(q: Annotated[list, Query()]=[]):
#     query_items = {"q": q}
#     return query_items

# Note: !!!IMPORTANT!!!
# Deprecating parameters
# Now let's say you don't like this parameter anymore.
#
# You have to leave it there a while because there are clients using it, but you want the docs to clearly show it as deprecated.
#
# Then pass the parameter deprecated=True to Query:

# =========> Path Parameters and Numeric Validations <=========

@app.get("/items/{item_id}")
async def read_items(
        item_id: Annotated[str, Path(title="This variable contains the identity of item", gt=0, le=1000)],
        q: Annotated[str, Query(max_length=43, gt=0, lt=0.5)] = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return  results
