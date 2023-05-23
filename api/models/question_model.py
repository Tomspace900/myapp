from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from configs.db_config import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    tally_id = Column(Integer)
    questionnaire_id = Column(Integer, ForeignKey("questionnaire.id"))
    text = Column(String(255))
    type = Column(String(50))
    is_mandatory = Column(Boolean)

    def __init__(self, tally_id, questionnaire_id, type, text, is_mandatory):
        self.tally_id = tally_id
        self.questionnaire_id = questionnaire_id
        self.text = text
        self.type = type
        self.is_mandatory = is_mandatory
