from configs.db_config import db


class Question(db.Model):
    __tablename__ = "Questions"

    id_question = db.Column(db.Integer, primary_key=True)
    tally_id_question = db.Column(db.Integer)
    questionnaire_id = db.Column(
        db.Integer, db.ForeignKey("Questionnaires.id_questionnaire"), nullable=False
    )
    label_question = db.Column(db.String(1000))
    type_question = db.Column(db.db.String(50))
    is_mandatory = db.Column(db.Boolean)

    # constructor
    def __init__(
        self,
        tally_id,
        questionnaire_id,
        type,
        label,
        is_mandatory,
    ):
        self.tally_id_question = tally_id
        self.questionnaire_id = questionnaire_id
        self.label_question = label
        self.type_question = type
        self.is_mandatory = is_mandatory


# alias
@property
def id(self):
    return self.id_question


def tally_id(self):
    return self.tally_id_question


def questionnaire_id(self):
    return self.questionnaire_id


def label(self):
    return self.label_question


def type(self):
    return self.type_question
