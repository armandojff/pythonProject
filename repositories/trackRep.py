from typing import List
from sqlalchemy.orm import Session
from models.tracks import Track
from schemas.trackSchema import TrackSchemaDetal




class TrackRepository:


    def get_song_by_id(self, TrackId:int, db: Session) -> TrackSchemaDetal:

        track: TrackSchemaDetal = db.query(Track).get(TrackId)

        return track

