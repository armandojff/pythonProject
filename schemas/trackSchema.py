from optparse import Option
from typing import Optional
from pydantic import BaseModel


class TrackSchema(BaseModel):

    AlbumId: int

    Name: Optional[str]

    Composer: Optional[str]

    class Config:
        orm_mode = True


class TrackSchemaDetal(BaseModel):

    TrackId: int
    
    Name: Optional[str]

    AlbumId: int

    MediaTypeId: int

    GenreId: int

    Composer: Optional[str]

    Milliseconds: int

    Bytes: int

    UnitPrice: float



    class Config:
        orm_mode = True

