#Import FastAPI class
from fastapi import FastAPI
#Create FastAPI instance and store it in app variable
app = FastAPI()
#Create path operation decorator
@app.get('/')
#Create path operation function for get requests to "/"" endpoint
async def root():
    return {'message': 'Hello World'}
