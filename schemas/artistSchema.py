from typing import Optional
from pydantic import BaseModel


class ArtistSchema(BaseModel):

    ArtistId: int

    Name: Optional[str]

    class Config:
        orm_mode = True


class ArtistNameSchema(BaseModel):

    Name: Optional[str]

    class Config:
        orm_mode = True
