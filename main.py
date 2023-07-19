from typing import Union
import graphene
from fastapi import FastAPI
#from starlette.middleware.cors import CORSMiddleware

from starlette_graphene3 import GraphQLApp

from app.schema import Mutation, Query

from app.config.setting import settings

#from app.routes import ping, product

app = FastAPI()

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))

@app.get("/")
async def ping():
    return {
        "ping": "pong!",
        "setting": settings
    }

'''
# Allowed Origins
origins = [
    "http://localhost",
    "http://localhost:8181",
    "http://localhost:5173",
    "*"
]

# App Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)
'''


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.post("/user")
# def createUser():
#     return {"message": "User has been created."}

'''
@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
'''
#app.include_router(ping.router)
#app.include_router(product.router, prefix="/products", tags=["products"])

host="0.0.0.0"
port=8000
app_name="app.main:app"

print(settings)

if __name__ == '__main__':
    Union.run(app_name, host=host, port=port)
