import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


# load environment variables
load_dotenv()

# username = os.getenv("MYSQL_USER")
# password = os.getenv("MYSQL_PASSWORD")
# name = os.getenv("MYSQL_NAME")
# host = os.getenv("MYSQL_HOST")
# port = os.getenv("MYSQL_PORT")

username = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
name = os.getenv("POSTGRES_NAME")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")

print("mysql ids :", username, password, name, host, port)


db = SQLAlchemy()

# local database url
# database_url = f"postgresql://{username}:{password}@{host}:{port}/{name}"

# heroku database url
database_url = "postgres://utxcufjowwlzjc:229a02feaba5f1793d4fc4b48e6525aa53b528c17dd249f56fa8b659edbae4c0@ec2-3-232-218-211.compute-1.amazonaws.com:5432/df036a9ud1tksk"
