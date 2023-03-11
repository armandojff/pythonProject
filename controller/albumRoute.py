from typing import List
from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from dependencies import get_db
from repositories.albumRep import AlbumRepository
from repositories.artistRep import ArtistRepository

from schemas.trackSchema import TrackSchema

router = APIRouter(tags=["Albums"])



@router.get("/albums/{id}",response_model=List[TrackSchema],status_code=status.HTTP_200_OK)
def get_songs_albums(id:int,db: Session = Depends(get_db),album_repository: AlbumRepository = Depends()) -> List[TrackSchema]:

    return album_repository.get_songs_albums(AlbumId=id,db=db)