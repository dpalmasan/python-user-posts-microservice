from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from types.pyobject_id import PyObjectId


class BlogPost(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    user_id: str
    title: str
    body: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    is_deleted: bool = False
    deleted_at: Optional[datetime] = None
