from configs.db_config import db
from models.question_model import Question


def create_question(questionnaire_id, question):
    question_tally_id = question["key"]
    question_text = question["label"]
    question_type = question["type"]
    is_mandatory = False

    question = Question(
        tally_id=question_tally_id,
        questionnaire_id=questionnaire_id,
        label=question_text,
        type=question_type,
        is_mandatory=is_mandatory,
    )

    # Add question to database
    db.session.add(question)
    db.session.commit()

    return question


def get_question(tally_id):
    question = db.session.query(Question).filter_by(tally_id_question=tally_id).first()
    if not question:
        return None

    return question
