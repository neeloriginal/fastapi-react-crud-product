from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
db_url="postgresql://postgres:Sajal%403692@localhost:5432/neeloriginal"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)