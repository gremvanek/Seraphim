from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

DATABASE_URL = "sqlite:///./test.db"

database = Database(DATABASE_URL)
metadata = MetaData()

Base = declarative_base()
engine = create_engine(DATABASE_URL)
