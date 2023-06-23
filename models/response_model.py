from configs.db_config import db


class Response(db.Model):
    __tablename__ = "responses"

    id_response = db.Column(db.Integer, primary_key=True)
    tally_id_responses = db.Column(db.String(6))
    id_questionnaire = db.Column(
        db.Integer, db.ForeignKey("questionnaires.id_questionnaire"), nullable=False
    )
    id_user = db.Column(db.Integer, db.ForeignKey("users.id_user"), nullable=False)
    date_soumission = db.Column(db.DateTime)

    def __init__(self, tally_id, questionnaire_id, user_id, submission_date):
        self.tally_id_responses = tally_id
        self.id_questionnaire = questionnaire_id
        self.id_user = user_id
        self.date_soumission = submission_date
