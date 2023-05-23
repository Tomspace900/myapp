from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# ! connection à la base de données mysql
db = create_engine("mysql+mysqlconnector://root:password@localhost:3306/test")

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()
