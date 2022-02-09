from pydantic import BaseModel, Field
from typing import List, Optional
from models.blog_post import BlogPost
from models.pyobject_id import PyObjectId
from bson import ObjectId


class BlogUser(BaseModel):
    """Implement user for blog.

    The field ``user_id`` is the user provided by other service (e.g.
    auth service).
    """

    id: Optional[PyObjectId] = Field(alias="_id")
    user_id: str
    name: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
