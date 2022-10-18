from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from configs.db import Base, engine
from controllers.basic_auth import current_user

app = FastAPI( # API Docs
    title='FastAPI', # app name
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

@app.get("/test")
def test_auth(credentials: HTTPBasicCredentials = Depends(current_user)):
    return {"msg": "gumagana"}