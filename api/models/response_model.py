from configs.db_config import db


class Response(db.Model):
    __tablename__ = "Responses"

    id_response = db.Column(db.Integer, primary_key=True)
    tally_id_responses = db.Column(db.Integer)
    id_questionnaire = db.Column(
        db.Integer, db.ForeignKey("Questionnaires.id_questionnaire"), nullable=False
    )
    id_user = db.Column(db.Integer, db.ForeignKey("Users.id_user"), nullable=False)
    submission_date = db.Column(db.DateTime)

    def __init__(self, tally_id, questionnaire_id, user_id, submission_date):
        self.tally_id_responses = tally_id
        self.id_questionnaire = questionnaire_id
        self.id_user = user_id
        self.submission_date = submission_date


@property
def id(self):
    return self.id_response


def tally_id(self):
    return self.tally_id_responses
