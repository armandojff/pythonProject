from typing import Optional
from pydantic import BaseModel


class AlbumsSchema(BaseModel):

    AlbumId: int

    Title: Optional[str]

    class Config:
        orm_mode = True


class AlbumsNameSchema(BaseModel):

    Title: Optional[str]

    class Config:
        orm_mode = True
