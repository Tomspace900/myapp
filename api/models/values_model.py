from api.configs.db_config import db


class Value(db.Model):
    __tablename__ = "values"

    id = db.Column(db.Integer, primary_key=True)
    response_id = db.Column(db.Integer, db.ForeignKey("response.id"), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"), primary_key=True)
    value = db.Column(db.String(255))

    def __init__(self, response_id, question_id, value):
        self.response_id = response_id
        self.question_id = question_id
        self.value = value
