from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://sql_app_user:QztL7UYGvyCUratCJ6gWeYOIMzYrReTK@dpg-cp65u8ol6cac738ehid0-a.frankfurt-postgres.render.com/sql_app"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
