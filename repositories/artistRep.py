from typing import List
from sqlalchemy.orm import Session
from models.albums import Album
from models.artist import Artist
from models.tracks import Track
from schemas.artistSchema import ArtistSchema
from schemas.albumSchema import AlbumsNameSchema,AlbumsSchema
from schemas.trackSchema import TrackSchema



class ArtistRepository:

    def get_all(self,db: Session) -> List[ArtistSchema]:

        artists_list: List[ArtistSchema] = db.query(Artist).all()

        return artists_list

    def get_albums_of_artist(self, ArtistId:int, db: Session) -> List[AlbumsSchema]:

        album_list: List[AlbumsSchema] = db.query(Album).filter(Album.ArtistId == ArtistId).all()

        return album_list

    def get_songs_of_artist(self, ArtistId:int, db: Session) -> List[TrackSchema]:

        artist_name: ArtistSchema = db.query(Artist).get(ArtistId)

        track_list: List[TrackSchema] = db.query(Track).filter(Track.Composer == artist_name.Name).all()

        return track_list



