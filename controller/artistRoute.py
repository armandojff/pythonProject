from typing import List
from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from dependencies import get_db
from repositories.artistRep import ArtistRepository
from schemas.artistSchema import ArtistNameSchema,ArtistSchema
from schemas.albumSchema import AlbumsNameSchema,AlbumsSchema
from schemas.trackSchema import TrackSchema

router = APIRouter(tags=["Singers"])


@router.get("/singers/",response_model=List[ArtistNameSchema],status_code=status.HTTP_200_OK)
def get_all(db: Session = Depends(get_db),artist_repository: ArtistRepository = Depends()) -> List[ArtistSchema]:

    return artist_repository.get_all(db)



@router.get("/singers/{id}",response_model=List[AlbumsNameSchema],status_code=status.HTTP_200_OK)
def get_albums_of_artist(id:int,db: Session = Depends(get_db),artist_repository: ArtistRepository = Depends()) -> List[AlbumsSchema]:

    return artist_repository.get_albums_of_artist(ArtistId=id,db=db)


    
@router.get("/singer/{id}",response_model=List[TrackSchema],status_code=status.HTTP_200_OK)
def get_songs_of_artist(id:int,db: Session = Depends(get_db),artist_repository: ArtistRepository = Depends()) -> List[TrackSchema]:

    return artist_repository.get_songs_of_artist(ArtistId=id,db=db)