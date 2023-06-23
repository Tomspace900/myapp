from configs.db_config import db


class HaveAccess(db.Model):
    __tablename__ = "have_access"

    id_questionnaire = db.Column(
        db.Integer, db.ForeignKey("questionnaires.id_questionnaire"), primary_key=True
    )
    id_user = db.Column(db.Integer, db.ForeignKey("users.id_user"), primary_key=True)

    # constructor
    def __init__(self, id_questionnaire, id_user):
        self.id_questionnaire = id_questionnaire
        self.id_user = id_user
