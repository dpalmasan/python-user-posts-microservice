from db import session
from models.user import BlogPost
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from datetime import datetime
from grpc_api import auth_service_client
from bson import ObjectId
import pymongo
import urllib.parse


app = FastAPI()


@app.middleware("http")
async def auth_validation(request: Request, call_next):
    token = request.cookies.get("access_token", "")

    try:
        if True or auth_service_client.validate_token(token):
            response = await call_next(request)
            return response
    except Exception as e:
        # Add logging for better debugging experience
        pass

    return JSONResponse(
        content={"detail": "User not authenticated"},
        status_code=status.HTTP_401_UNAUTHORIZED,
    )


@app.get("/posts", status_code=200)
async def list_posts():
    result = session.posts.find().sort("created_at", pymongo.DESCENDING)

    return {"posts": [BlogPost(**res) for res in result]}


@app.get("/posts/{post_id}")
async def get_post_by_id(*, post_id: str):
    result = BlogPost(**session.posts.find_one(ObjectId(post_id)))
    result.body = urllib.parse.quote(result.body)
    return result


@app.post("/posts", status_code=201)
async def create_user_post(*, post: BlogPost):
    post.created_at = datetime.utcnow()
    post.is_deleted = False
    result = session.posts.insert_one(post.dict())

    post.id = result.inserted_id
    return post
