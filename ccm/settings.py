import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = os.environ.get('DB_URL')
TEST_DB_URL = os.environ.get('TEST_DB_URL')

db_engine = create_engine(DB_URL)

Base = declarative_base()
Session = sessionmaker(bind=db_engine)
session = Session()
