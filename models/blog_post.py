from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional
from models.pyobject_id import PyObjectId
from bson import ObjectId


class BlogPost(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    user_id: PyObjectId
    title: str
    body: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: Optional[datetime] = None
    is_deleted: bool = False
    deleted_at: Optional[datetime] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
