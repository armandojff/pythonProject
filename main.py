from cgi import test
from xml.dom.minidom import AttributeList
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config_db.db import Base,engine
from models.artist import Artist
from controller.artistRoute import router as artist_url
from controller.albumRoute import router as album_url
from controller.songRoute import router as song_url



def get_application():

    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="FastAPI Armando Fernandes P2", description="C.I 25716890")


    app.add_middleware(CORSMiddleware,allow_origins=[""],allow_credentials=True,allow_methods=[""],allow_headers=["*"])

    app.include_router(artist_url,prefix="/music-store/api/v1")

    app.include_router(album_url,prefix="/music-store/api/v1")

    app.include_router(song_url,prefix="/music-store/api/v1")


    return app


app = get_application()