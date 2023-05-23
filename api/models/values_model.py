from sqlalchemy import Column, Integer, String, ForeignKey
from configs.db_config import Base


class Value(Base):
    __tablename__ = "values"

    id = Column(Integer, primary_key=True)
    response_id = Column(Integer, ForeignKey("response.id"), primary_key=True)
    question_id = Column(Integer, ForeignKey("question.id"), primary_key=True)
    value = Column(String(255))

    def __init__(self, response_id, question_id, value):
        self.response_id = response_id
        self.question_id = question_id
        self.value = value
