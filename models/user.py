from typing import Optional

from bson import ObjectId
from pydantic import BaseModel
from pydantic import Field

from models.pyobject_id import PyObjectId


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
