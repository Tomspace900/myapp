from api.configs.db_config import db


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    tally_id = db.Column(db.Integer)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey("questionnaire.id"))
    text = db.Column(db.String(255))
    type = db.Column(db.String(50))
    is_mandatory = db.Column(db.Boolean)

    def __init__(self, tally_id, questionnaire_id, type, text, is_mandatory):
        self.tally_id = tally_id
        self.questionnaire_id = questionnaire_id
        self.text = text
        self.type = type
        self.is_mandatory = is_mandatory
