from db import session
from models.pyobject_id import PyObjectId
from models.user import BlogPost
from fastapi import FastAPI


app = FastAPI()


@app.get("/posts/{user_id}")
async def list_posts_from_user(*, user_id: str):
    return {
        "user_id": user_id,
        "posts": [
            BlogPost(**post)
            for post in session.posts.find({"user_id": PyObjectId(user_id)})
        ],
    }
