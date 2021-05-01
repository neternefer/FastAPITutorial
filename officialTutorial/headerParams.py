'''
By default, Header will convert the parameter names
characters from underscore (_) to hyphen (-) to extract and document the headers.
You can turn off that behaviour by setting the parameter convert_underscores of Header to False:
async def read_item(user_agent: Optional[str] = Header(None, convert_underscores=False))
'''

from typing import Optional, List
from fastapi import FastAPI, Header #import Header

app = FastAPI()

@app.get("/items/")
async def read_item(user_agent: Optional[str] = Header(None)): #declare Header param
    return {"User-Agent": user_agent}

#It is possible to receive duplicate headers. That means, the same header with multiple values.
#You can define those cases using a list in the type declaration.
#You will receive all the values from the duplicate header as a Python list.

@app.get("/things/")
async def read_tokens(x_token: Optional[List[str]] = Header(None)):
    return {"X-Token values": x_token}