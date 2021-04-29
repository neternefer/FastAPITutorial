from fastapi import FastAPI
from typing import Optional

app = FastAPI()

#When you declare other function parameters that
#are not part of the path parameters, they are automatically
#interpreted as "query" parameters.

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10): #Default
    return fake_items_db[skip : skip + limit]

#The query is the set of key-value pairs that go after the ? in a URL,
#separated by & characters.
#They are not a fixed part of a path, they can be optional and can have default values.
#http://127.0.0.1:800/items/ = http://127.0.0.1:8000/items/?skip=0&limit=10

#You can declare optional query parameters, by setting their default to None
@app.get("/itemss/{item_id}")
async def get_item(item_id: str, q: Optional[str] = None): #Optional q param
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

#http://127.0.0.1:8000/itemss/12?q=blabla -> {
#                                               "item_id": "12",
#                                               "q": "blabla" }

#Bool values converted
@app.get("/itemsss/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

#http://127.0.0.1:8000/items/foo?short=1 -> short=True/true/on/yes

#You can declare multiple path parameters and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

#http://127.0.0.1:8000/users/12/items/fruit2?q=banana&short=false

#To make non-path param REQUIRED, don't set its default value
#The failure to include that param will result in error message
#{"detail":[{"loc":["query","need"],"msg":"field required","type":"value_error.missing"}]}
@app.get("/things/{thing_id}")
async def get_thing(thing_id: int, need: str):
    item = {"thing_id": thing_id, "need": need}
    return item

#http://127.0.0.1:8000/things/12?need=yes -> no error