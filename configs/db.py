from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .env import DB_URI

engine = create_engine(DB_URI)
SessionLocal = sessionmaker(autocommit=False, bind=engine)
Base = declarative_base()