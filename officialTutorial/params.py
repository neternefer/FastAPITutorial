from fastapi import FastAPI
from enum import Enum

app = FastAPI()

#Path parameters
#Use syntax similar to string formatting
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

#The value of the path parameter item_id will be passed
#to your function as the argument item_id.
#You can declare the param type for data validation
#http://127.0.0.1:8000/items/foo -> {"detail":[{"loc":["path","item_id"],
#                                   "msg":"value is not a valid integer",
#                                   "type":"type_error.integer"}]}
#http://127.0.0.1:8000/items/234 -> {"item_id": 234}

#Path params are read in order, fixed path must come before param path

#Predefine valid param values as fixed class attributes/enumeration members
class FruitModel(str, Enum):
    apple = "apple"
    pear = "pear"
    grape = "grape"

@app.get("/fruits/{fruit}")
async def get_fruit(fruit: FruitModel):
    if fruit == FruitModel.apple:
        return {"fruit": fruit, "message": "Apple Pie"}
    if fruit.value == FruitModel.pear: #or FruitModel.pear.value
        return {"fruit": fruit, "message": "Pear Pie"}
    return {"fruit": fruit, "message": "Whatever"}

#Path params containing paths
#e.g. files/{file_path} -> file_path = user1/docs/new.txt
#Using Starlette tool you can declare a path parameter containing a path :
#/files/{file_path:path} -> this param should match any path
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}