# FastAPI generates a "schema" with all your API using the OpenAPI standard for defining APIs.

"""POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data."""
# =========> Main Code <=========
from fastapi import FastAPI, Cookie, Header, Query, Path, Body, Response  # FastAPI is a Python class that provides all the functionality for your API.
from enum import Enum
from pydantic import BaseModel, HttpUrl, Field #WARNING: Notice that Field is imported directly from pydantic, not from fastapi as are all the rest (Query, Path, Body, etc).
from typing import Annotated, Any
from datetime import date, datetime, time, timedelta
from uuid import UUID
from fastapi.responses import  JSONResponse, RedirectResponse

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

# @app.get("/items/{item_id}")
# async def read_items(
#         item_id: Annotated[str, Path(title="This variable contains the identity of item", gt=0, le=1000)],
#         q: Annotated[str, Query(max_length=43, gt=0, lt=0.5)] = None
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return  results

# =========> Body - Multiple Parameters <=========

# class Item(BaseModel):
#     name: str
#     price: int
#     description: str | None
#     tax: int | None
#
# class User(BaseModel):
#     name: str
#     full_name: str
#
# @app.put("/items")
# def update_item(
#         item_id: Annotated[int | None, Path(title="It contains list of all the items", ge=3, le=32)] = None,
#         q: str | None = None,
#         item: Annotated[Item | None, Body(embed=True)] = None
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results
#
# """{
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     }
# }"""
#
# @app.get("/items/{item_id}")
# def update_user(
#         item_id: str,
#         item: Item,
#         user: User,
#         importance: Annotated[int, Body(gt = 0)], TODO: Understand what body does?
#         q : str | None = None
# ):
#     results = {"item_id": item_id, "user": user, "item": item, "importance": importance}
#     if q: results.update({"q": q})
#     return results

# =========> Body - Fields <=========
# class BaseItem(BaseModel):
#     name: str
#     description: str | None = Field(title="This is the tile of the item", max_length=50)
#     price: int = Field(gt = 0, description="it must be greater than zero")
#     tax: int
#
# @app.put("/items/{item_id}")
# async def get_item(item_id: str, item: Annotated[BaseItem, Body(embed=True)]):
#     return {"item": item, "item_id": item_id}

# =========> Body - Nested Models <=========
# class Image(BaseModel):
#     name: str
#     url: HttpUrl
#
# class BaseItem(BaseModel):
#     name: str
#     description: str | None
#     price: int
#     tax: int | None
#     # tags : list[str] = []
#     tags: set[str] = set()
#     image: list[Image] | None = None
#
# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[BaseItem]
#
# """{
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2,
#     "tags": [
#         "rock",
#         "metal",
#         "bar"
#     ],
#     "images": [
#         {
#             "url": "http://example.com/baz.jpg",
#             "name": "The Foo live"
#         },
#         {
#             "url": "http://example.com/dave.jpg",
#             "name": "The Baz"
#         }
#     ]
# }"""
#
# @app.put("item/{item_id}")
# async def update_item(item: BaseItem, item_id: int):
#     results = {"item": item, "item_id": item_id}
#
# @app.post("/offers")
# async def create_offer(offer: Offer):
#     return Offer
#
# @app.post("/images/multiple")
# async def create_multiple_images(images: list[Image]):
#     return images
#
# @app.post("/index-weights/")
# async def create_index_weights(weights: dict[int, float]):
#     return weights

# =========> Declare Request Example Data <=========
# class Item(BaseModel):
#     name: str = Field(examples=["Foo"])
#     description: str | None = Field(examples=["A very long Text"])
#     price: float = Field(examples=[3])
#     tax: float | None = Field(examples=[2.0])
#
#     model_config = {
#         "json_extra_schema": {
#             "examples": [
#                 {
#                     "name": "Foo",
#                     "description": "A long text",
#                     "price": 21.32,
#                     "tax": 23.32,
#                  }
#             ]
#         }
#     }
#
# @app.put("/items/{item_id}")
# async def update_item(
#         item_id: int, item: Annotated[Item, Body(examples=[{
#             "name": "Foo",
#             "description": "A long text",
#             "price": 21.32,
#             "tax": 23.32,
#         }])] #You can of course also pass multiple examples
# ): #You can declare the OpenAPI-specific examples in FastAPI with the parameter openapi_examples
#     return {"item_id": item_id, "item": item}

# =========> Extra Data Types <=========
#
# @app.put("/items/{item_id}")
# async def read_items(
#         item_id: Annotated[UUID | None, Body()] = None,
#         start_datetime: Annotated[datetime | None, Body()] = None,
#         end_datetime : Annotated[datetime | None, Body()] = None,
#         repeat_at: Annotated[time | None, Body()] = None,
#         process_after: Annotated[timedelta | None, Body()] = None,
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration,
#     }

# =========> Cookie Parameters <=========

# @app.get("/items")
# async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
#     return {"ads_id": ads_id}

# =========> Header Parameters <=========
#
# @app.get('/items')
# async def read_items(user_agent: Annotated[list[str] | None, Header(convert_underscores=False)]= None):
#     return {"user_agent": user_agent}

# =========> Response Model - Return Type <=========

class BaseItem(BaseModel):
    name: str
    price: int
    tax: int | None = None
    description: str | None = None
    tags: list[str] = []

@app.post('/items')
async def add_item(item: BaseItem) -> BaseItem:
    return item

#If you declare both a return type and a response_model, the response_model will take priority and be used by FastAPI.

@app.get("/items", response_model=list[BaseItem])
async def get_item() -> Any:
    return [
        {"name": "yash", "price": 32},
        {"name": "sai", 'price': 322},
    ]

class BaseUser(BaseModel):
    username: str
    email: str
    fullname: str | None = None
class UserIn(BaseUser):
    password: str

# class UserOut(BaseModel):
#     username: str
#     email: str
#     fullname: str | None = None

# @app.post("/user", response_model= UserOut)
@app.post("/user")
async def create_user(user: UserIn) -> BaseUser:
    return user

@app.get('/portal')
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})

@app.get('/foo', response_model=None)
async def foo(bar: bool = False) -> JSONResponse | dict:
    return JSONResponse(content={"Foo": "bar"})

# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}

app.get("/items/{item_id}/name",
        response_model= BaseItem,
        response_model_include= {"name", "description"})
async def read_item(item_id: str):
    return items[item_id]

app.get("/items/{item_id}/public",
        response_model= BaseItem,
        response_model_exclude= {"tax"})  #If you forget to use a set and use a list or tuple instead, FastAPI will still convert it to a set and it will work correctly:
async def read_item_public(item_id: str):
    return items[item_id]

