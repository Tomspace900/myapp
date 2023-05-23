from api.configs.db_config import db


class Response(db.Model):
    __tablename__ = "responses"

    id = db.Column(db.Integer, primary_key=True)
    tally_id = db.Column(db.Integer)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey("questionnaire.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    submission_date = db.Column(db.DateTime)

    def __init__(self, tally_id, questionnaire_id, user_id, submission_date):
        self.tally_id = tally_id
        self.questionnaire_id = questionnaire_id
        self.user_id = user_id
        self.submission_date = submission_date
