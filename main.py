import urllib.parse
from datetime import datetime

import pymongo
from bson import ObjectId
from fastapi import FastAPI
from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse

from db import session
from grpc_api import auth_service_client
from models.blog_post import BlogPost
from models.blog_post import PartialBlogPost
from utils.auth import get_claims_from_token


app = FastAPI()


# Disabled to test auth on API gateway
# @app.middleware("http")
async def auth_validation(request: Request, call_next):
    token = request.cookies.get("access_token", "")

    try:
        if auth_service_client.validate_token(token):
            response = await call_next(request)
            return response
    except Exception as e:
        # Add logging for better debugging experience
        print(e)
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
    post = session.posts.find_one(ObjectId(post_id))
    if post is None:
        return {}
    result = BlogPost(**post)
    result.body = urllib.parse.quote(result.body)
    return result


@app.patch("/posts/{post_id}")
async def update_post_by_id(*, post_id: str, post: PartialBlogPost):
    post.updated_at = datetime.now()
    post_dict = post.dict(exclude_unset=True)
    result = session.posts.update_one(
        {"_id": ObjectId(post_id)}, {"$set": post_dict}
    )
    if result.modified_count == 0:
        return {}
    updated_post = session.posts.find_one(ObjectId(post_id))

    result = BlogPost(**updated_post)
    result.body = urllib.parse.quote(result.body)
    return result


@app.post("/posts", status_code=201)
async def create_user_post(*, req: Request, post: PartialBlogPost):
    jwt_token = req.headers["Authorization"].split()[1]
    user_id = get_claims_from_token(jwt_token)["user_id"]
    post.user_id = user_id
    post.created_at = datetime.utcnow()
    post.is_deleted = False
    result = session.posts.insert_one(post.dict())

    post.id = result.inserted_id
    return post
