from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


SQL_DB_URL = os.getenv("DB_CONN_STR")

engine = create_engine(SQL_DB_URL)

session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
