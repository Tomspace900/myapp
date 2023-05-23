from sqlalchemy import Column, Integer, DateTime, ForeignKey
from configs.db_config import Base


class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True)
    tally_id = Column(Integer)
    questionnaire_id = Column(Integer, ForeignKey("questionnaire.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    submission_date = Column(DateTime)

    def __init__(self, tally_id, questionnaire_id, user_id, submission_date):
        self.tally_id = tally_id
        self.questionnaire_id = questionnaire_id
        self.user_id = user_id
        self.submission_date = submission_date
