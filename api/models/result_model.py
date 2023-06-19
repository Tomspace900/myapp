from configs.db_config import db


class Result(db.Model):
    __tablename__ = "results"

    id_question = db.Column(
        db.Integer, db.ForeignKey("Questions.id_question"), primary_key=True
    )
    id_response = db.Column(
        db.Integer, db.ForeignKey("Responses.id_response"), primary_key=True
    )
    results = db.Column(db.String(100))

    # constructor
    def __init__(self, id_question, id_response, results):
        self.id_question = id_question
        self.id_response = id_response
        self.results = results

