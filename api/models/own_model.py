from configs.db_config import db


class Own(db.Model):
    __tablename__ = "own"

    id_questionnaire = db.Column(
        db.Integer, db.ForeignKey("Questionnaires.id_questionnaire"), primary_key=True
    )
    id_question = db.Column(
        db.Integer, db.ForeignKey("Questions.id_question"), primary_key=True
    )

    # constructor
    def __init__(self, id_questionnaire, id_question):
        self.id_questionnaire = id_questionnaire
        self.id_question = id_question
