from pydantic import BaseModel, Field
from typing import List, Optional


class FavMuseum(BaseModel):
    user_id: str
    fav_id: int


class MuseumId(BaseModel):
    museum_id: int
    user_id: str


class UserId(BaseModel):
    user_id: str

