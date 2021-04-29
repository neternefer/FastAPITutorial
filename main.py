#Import FastAPI class
#Import List for generic and internal types(type parameters)
from fastapi import FastAPI
from typing import List, Set, Tuple, Dict, Optional
#Create FastAPI instance and store it in app variable
app = FastAPI()
#Create path operation decorator
@app.get('/')
#Create path operation function for get requests to "/"" endpoint
async def root():
    return {'message': 'Hello World'}

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
