############ Intro ############

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_age(first_name: str, age: int):
    return f"{first_name} is {str(age)} years old"

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b,item_c,  item_d, item_d, item_e

def process_item(items: list[str]):
    for item in items:
        print(item)

def new_process_items(item_t: tuple[str, str, int], item_s: set[bytes]):
    return item_t, item_s

def dict_process_items(item_d:dict[str: int]):
    return item_d

#there's also a new syntax where you can put the possible types separated by a vertical bar (|).

def say_hi(name: str | None):
    print(f"Hey {name}")

class Person:
    def __init__(self, name: str):
        self.name = name

def get_name(one_person: Person):
    return one_person.name

if __name__ == "__main__":
    print(get_full_name("jhon", "doe"))
    print(get_age("jhon", 32))
    say_hi("yash")
    say_hi(name=None)

############ PYDENTIC ############

from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "Jhon Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data= {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)
print(user)
print(user.id)

############ MetaData Annotation ############
"""Python also has a feature that allows putting additional metadata in these type hints using Annotated. Python
itself doesn't do anything with this Annotated. And for editors and other tools, the type is still str. But you can
use this space in Annotated to provide FastAPI with additional metadata about how you want your application to 
behave."""
from typing import Annotated

def say_hello(name : Annotated[str, "This is just some metadata"]) -> str:
    return f"Hello {name}"

print(say_hello("yash"))