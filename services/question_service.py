from configs.db_config import db
from models.question_model import Question
from models.own_model import Own


def create_question(question, questionnaire_id):
    question_tally_id = question["key"][-6:]
    question_text = question["label"]
    question_type = question["type"]
    is_mandatory = False

    question = Question(
        tally_id=question_tally_id,
        label=question_text,
        type=question_type,
        is_mandatory=is_mandatory,
    )

    # Add question to database
    db.session.add(question)
    db.session.commit()

    # Add question to own table
    Own(questionnaire_id, question.id_question)

    return question


def get_question(tally_id):
    question = db.session.query(Question).filter_by(tally_id_question=tally_id).first()
    if not question:
        return None

    return question
