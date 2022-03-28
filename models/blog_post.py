from datetime import datetime
from datetime import timezone
from typing import List
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel
from pydantic import Field

from models.pyobject_id import PyObjectId


class PartialBlogPost(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    user_id: Optional[PyObjectId] = None
    title: Optional[str] = None
    body: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_deleted: bool = False
    deleted_at: Optional[datetime] = None
    tags: Optional[List[str]] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class BlogPost(PartialBlogPost):
    id: Optional[PyObjectId] = Field(alias="_id")
    user_id: Optional[PyObjectId] = None
    title: str
    body: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: Optional[datetime] = None
    is_deleted: bool = False
    deleted_at: Optional[datetime] = None
    tags: Optional[List[str]] = None
