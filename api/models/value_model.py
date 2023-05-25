from configs.db_config import db


class Value(db.Model):
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


# alias
@property
def id_question(self):
    return self.id_question


def id_response(self):
    return self.id_response


def value(self):
    return self.results
