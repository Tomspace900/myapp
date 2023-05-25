import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


# load environment variables
load_dotenv()

username = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
database = os.getenv("DATABASE_NAME")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")

print("mysql ids :", username, password, database, host, port)


db = SQLAlchemy()

database_url = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"
