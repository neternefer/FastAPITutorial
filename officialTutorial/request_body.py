# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
"""
A request body is data sent by the client to your API.
A response body is the data your API sends to the client.

Your API almost always has to send a response body.
But clients don't necessarily need to send request bodies all the time.

To declare a request body, you use Pydantic models
"""
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel): #declare data model as a class
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

#when a model attribute has a default value, it is not required

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item): #declare it as func param with a type of the model
    item_dict = item.dict() #.dict() will provide a dict of fields and can take other arguments.
    price_with_tax = item.price + item.tax
    item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

#You can declare path/query parameters and request body at the same time.

#FastAPI will recognize that the function parameters that match path parameters
#should be taken from the path, singular type params are query params
#and that function parameters that are declared to be
#Pydantic models should be taken from the request body.
@app.post("/newItems/{item_id}")
def create_new(item_id: int, item: Item, q: Optional[str] = None):
    result =  {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result