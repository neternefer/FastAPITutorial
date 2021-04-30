'''
FastAPI allows you to declare additional information and
validation for your parameters.
Optional[x] isn't used by the API but setting a default None
value flags it as a non-required param.
To add additional validation, use Query as default value.
Optional[x] = None == Optional[x] = Query(None) -> explicit query param declaration

Values other than None can be passed as a first argument to
be used as the default value.
-> async def read_items(q: str = Query("fixedquery", min_length=3)):
'''
from typing import Optional, List
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def get_items(q: Optional[str] = Query(
        None,  #first Query param sets default value
        min_length=3,
        max_length=50,
        regex="^fixedquery$")):
    results = {"items": [{"item_1": "item_1"}, {"item_2": "item_2"}]}
    if q:
        results.update({"q": q})
    return results

#When you need to declare a value as required while using Query,
#you can use ... as the first argument:
@app.get("/things/")
async def get_things(q: Optional[str] = Query(
        ...,  #this sets the q param as required
        min_length=3)):
    results = {"items": [{"item_1": "item_1"}, {"item_2": "item_2"}]}
    if q:
        results.update({"q": q})
    return results

#When you define a query parameter explicitly with Query you can also
#declare it to receive a list of values, or said in other way, to receive multiple values.
#For example, to declare a query parameter q that can appear multiple times in the URL:
@app.get("/morethings")
async def get_more(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items

#http://127.0.0.1:8000/morethings?q=bla&q=foo&q=bar&q=string
#-> {
#  "q": [
#    "bla",
#    "foo",
#    "bar",
#    "string"
#  ]
#}

#You can provide a default list of values
#async def read_items(q: List[str] = Query(["foo", "bar"])):

#You can use list directly but its contents won't be checked
#async def read_items(q: list = Query([])):

#You can declare more metadata which will be used for documentation/by tools
#async def get_this(q: Optional[str] = Query(None, title="Query string", description="blabla"))

#You can declare param alias which will be used to find its value:
#async def get_that(q: Optional[str] = Query(None, max_length=30, alias="item-query"))

#To flag the param as deprecated (as it may still be used by some clients):
#async def get_sth(q: Optional[str] = Query(None, deprecated=True)


