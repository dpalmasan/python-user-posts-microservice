from db import session
from models.pyobject_id import PyObjectId
from models.user import BlogPost
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from datetime import datetime


app = FastAPI()


@app.middleware("http")
async def auth_required(request: Request, call_next):
    auth_string = request.cookies.get("access_token")
    if auth_string is not None and auth_string == "djsaksdhADSJHDSA17823":
        response = await call_next(request)
        return response

    return JSONResponse(
        content={"detail": "Not authorized"},
        status_code=status.HTTP_401_UNAUTHORIZED,
    )


@app.get("/posts/{user_id}")
async def list_posts_from_user(*, user_id: str):
    return {
        "user_id": user_id,
        "posts": [
            BlogPost(**post)
            for post in session.posts.find({"user_id": PyObjectId(user_id)})
        ],
    }


@app.post("/posts", status_code=201)
async def create_user_post(*, post: BlogPost):
    post.created_at = datetime.utcnow()
    post.is_deleted = False
    result = session.posts.insert_one(post.dict())

    post.id = result.inserted_id
    return post
