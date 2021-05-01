'''
You can define Cookie parameters the same way you define
Query and Path parameters.
Cookie is a "sister" class of Path and Query.
It also inherits from the same common Param class.

But remember that when you import Query, Path, Cookie
and others from fastapi, those are actually functions
that return special classes.
'''
from typing import Optional
from fastapi import FastAPI, Cookie #import Cookie

app = FastAPI()

@app.get("/items/")
async def read_item(item_id: Optional[str] = Cookie(None)): #declare Cookie params, first = default
    return {"item_id": item_id}