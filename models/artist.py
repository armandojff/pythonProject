from sqlalchemy import Integer,Column,String
from sqlalchemy.orm import relationship
from config_db.db import Base

class Artist(Base):

    __tablename__ = 'artists'

    ArtistId = Column(Integer, primary_key=True)

    Name = Column(String(120))