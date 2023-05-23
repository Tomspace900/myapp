from sqlalchemy import Column, Integer, String
from configs.db_config import Base


class Questionnaire(Base):
    __tablename__ = "questionnaires"

    id = Column(Integer, primary_key=True)
    tally_id = Column(Integer)
    name = Column(String(255))

    def __init__(self, tally_id, name):
        self.tally_id = tally_id
        self.name = name
