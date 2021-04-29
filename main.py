# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

#Import List etc for generic and internal types(type parameters)
#Import Pydantic model
from typing import List, Set, Tuple, Dict, Optional
from datetime import datetime
from pydantic import BaseModel

#Generic types
def process_items(items: List[str]):
    for item in items:
        print(item)

def process_items_ts(items_t: Tuple[str, str, int], items_s: Set[bytes]):
    return items_t, items_s

def process_items_d(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

#Optional declares that a variable has a type, like str, but that it is "optional",
#which means that it could also be None e.g. user didn't provide their name

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f'Hey {name}!')
    else:
        print('Hello World')

#It's possible to declare classes as types
class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

#Pydantic models
#You declare the "shape" of the data as classes with attributes. Each attribute has a type.
#Then you create an instance of that class with some values and it will validate the values,
#convert them to the appropriate type (if that's the case) and give you an object with all the data.
class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
print(user.id)

