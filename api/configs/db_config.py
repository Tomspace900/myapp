import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# load environment variables
load_dotenv()

username = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
database = os.getenv("DATABASE_NAME")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")

print(username, password, database, host, port)

# connect to mysql database
db = create_engine(
    f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"
)

# create session for queries
Session = sessionmaker(bind=db)
session = Session()

# create base class for models
Base = declarative_base()
