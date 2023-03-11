from typing import List
from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from dependencies import get_db
from repositories.albumRep import AlbumRepository
from repositories.artistRep import ArtistRepository
from repositories.trackRep import TrackRepository

from schemas.trackSchema import TrackSchema

from schemas.trackSchema import TrackSchemaDetal

router = APIRouter(tags=["song"])



@router.get("/song/{id}",response_model=TrackSchemaDetal,status_code=status.HTTP_200_OK)
def get_song_by_id(id:int,db: Session = Depends(get_db),track_repository: TrackRepository = Depends()) -> TrackSchemaDetal:

    return track_repository.get_song_by_id(TrackId=id,db=db)