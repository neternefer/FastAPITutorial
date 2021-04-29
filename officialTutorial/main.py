#Import FastAPI class which inherits from Starlette
from fastapi import FastAPI
#Create FastAPI instance and store it in app variable
app = FastAPI()
#Create path operation decorator
@app.get('/')
#Create path operation function for get requests to "/"" endpoint
async def root():
    return {'message': 'Hello World'}
#A "path" is also commonly called an "endpoint" or a "route" and
#refers to the last part of the URL starting from the first /.
#"Operation" here refers to one of the HTTP "methods".


#uvicorn main:app --reload
#This will start the server at http://127.0.0.1:8000
#main is the name of Python module, app is the name of the FastAPI instance

#OpenAPI defines an API schema for your API. And that schema includes
#definitions (or "schemas") of the data sent and received by your API using
#JSON Schema, the standard for JSON data schemas.

