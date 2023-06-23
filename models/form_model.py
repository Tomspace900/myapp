from configs.db_config import db


class Questionnaire(db.Model):
    __tablename__ = "questionnaires"

    id_questionnaire = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tally_id_questionnaire = db.Column(db.String(6))
    name_questionnaire = db.Column(db.String(100))
    date_creation_questionnaire = db.Column(db.DateTime)

    # constructor
    def __init__(self, tally_id, name, date_creation):
        self.tally_id_questionnaire = tally_id
        self.name_questionnaire = name
        self.date_creation_questionnaire = date_creation
