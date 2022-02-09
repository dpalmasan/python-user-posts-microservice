from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BlogPost(BaseModel):
    user_id: str
    title: str
    body: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    is_deleted: bool = False
    deleted_at: Optional[datetime] = None
