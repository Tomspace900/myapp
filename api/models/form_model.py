from configs.db_config import db


class Questionnaire(db.Model):
    __tablename__ = "Questionnaires"

    id_questionnaire = db.Column(db.Integer, primary_key=True)
    tally_id_questionnaire = db.Column(db.Integer)
    name_questionnaire = db.Column(db.String(100))
    date_creation_questionnaire = db.Column(db.DateTime)

    # constructor
    def __init__(self, tally_id, name):
        self.tally_id_questionnaire = tally_id
        self.name_questionnaire = name


# alias
@property
def id(self):
    return self.id_questionnaire


def tally_id(self):
    return self.tally_id_questionnaire


def name(self):
    return self.name_questionnaire


def date_creation(self):
    return self.date_creation_questionnaire
