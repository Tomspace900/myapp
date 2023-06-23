from configs.db_config import db
from models.have_access_model import HaveAccess


def create_own(questionnaire_id, question_id):
    have_access = HaveAccess(questionnaire_id, question_id)

    # Add association to database
    db.session.add(have_access)
    db.session.commit()

    return have_access
