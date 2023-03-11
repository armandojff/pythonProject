from typing import List
from sqlalchemy.orm import Session
from models.tracks import Track
from models.artist import Artist
from schemas.trackSchema import TrackSchema




class AlbumRepository:


    def get_songs_albums(self, AlbumId:int, db: Session) -> List[TrackSchema]:

        track_list: List[TrackSchema] = db.query(Track).filter(Track.AlbumId == AlbumId).all()

        return track_list


