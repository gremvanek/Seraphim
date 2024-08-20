from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

DATABASE_URL = "sqlite:///./test.db"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()