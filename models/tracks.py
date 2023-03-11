from sqlalchemy import Integer,Column,String,Numeric
from sqlalchemy.orm import relationship
from config_db.db import Base

class Track(Base):

    __tablename__ = 'tracks'

    TrackId = Column(Integer, primary_key=True)

    Name = Column(String(120))

    AlbumId = Column(Integer)

    MediaTypeId = Column(Integer)

    GenreId = Column(Integer)

    Composer = Column(String(120))

    Milliseconds = Column(Integer)

    Bytes = Column(Integer)

    UnitPrice = Column(Numeric(10, 2))
