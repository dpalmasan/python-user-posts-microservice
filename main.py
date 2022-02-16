from db import session
from models.pyobject_id import PyObjectId
from models.user import BlogPost
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from datetime import datetime
from grpc_api import auth_service_client


app = FastAPI()


@app.middleware("http")
async def auth_validation(request: Request, call_next):
    token = request.cookies["access_token"]

    try:
        if auth_service_client.validate_token(token):
            response = await call_next(request)
            return response
    except Exception:
        pass

    return JSONResponse(
        content={"detail": "User not authenticated"},
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
