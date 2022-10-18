from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configs.db import Base, engine

app = FastAPI( # API Docs
    title='', # app name
    description='Powered by FastAPI',
    version='1.0.1',
    docs_url="/api/docs",
    redoc_url="/api/redocs",
)

Base.metadata.create_all(engine)

origins = ["*"] # WILDCARD ALL ACCESS

app.add_middleware( # MIDDLEWARE CONFFIG
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)