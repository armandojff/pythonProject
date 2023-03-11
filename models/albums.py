from sqlalchemy import Integer,Column,String
from sqlalchemy.orm import relationship
from config_db.db import Base

class Album(Base):

    __tablename__ = 'albums'

    AlbumId = Column(Integer, primary_key=True)

    Title = Column(String(160))

    ArtistId = Column(Integer)
