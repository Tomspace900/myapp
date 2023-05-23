from api.configs.db_config import db


class Questionnaire(db.Model):
    __tablename__ = "questionnaires"

    id = db.Column(db.Integer, primary_key=True)
    tally_id = db.Column(db.Integer)
    name = db.Column(db.String(255))

    def __init__(self, tally_id, name):
        self.tally_id = tally_id
        self.name = name
