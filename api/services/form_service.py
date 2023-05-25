from configs.db_config import db
from models.form_model import Questionnaire
from services.user_service import create_user
from services.response_service import create_response
from services.question_service import create_question, get_question
from services.value_service import create_value


def create_form(tally_id, form_name, questions):
    # Check if questionnaire already exists
    existing_form = (
        db.session.query(Questionnaire)
        .filter_by(tally_id_questionnaire=tally_id)
        .first()
    )
    if existing_form:
        return existing_form

    questionnaire = Questionnaire(tally_id=tally_id, name=form_name)

    # Create questions
    for question in questions:
        create_question(questionnaire.id, question)

    # Add questionnaire to database
    db.session.add(questionnaire)
    db.session.commit()
    return questionnaire


def save_form(data):
    response_data = data[0]["data"]
    form_name = response_data["formName"]
    tally_id = response_data["formId"]
    user_tally_id = response_data["respondentId"]
    response_tally_id = response_data["responseId"]
    submission_date = response_data["createdAt"]
    questions = response_data["fields"]

    # Create form
    questionnaire = create_form(tally_id, form_name, questions)

    # Create user
    user = create_user(user_tally_id, None, None, False)

    # Create response (submission)
    response = create_response(
        response_tally_id, questionnaire.id, user.id, submission_date
    )

    # Create values to questions
    for question in questions:
        question_tally_id = question["key"]
        question = get_question(question_tally_id)
        if not question:
            question = create_question(questionnaire.id, question)

        response_value = question["value"]

        # If question is multiple choice, get the text of the option
        if question["type"] == "MULTIPLE_CHOICE":
            for option in question["options"]:
                if option["id"] == response_value:
                    response_value = option["text"]
                    break

        create_value(response.id, question.id, response_value)

    return questionnaire.id


def get_form(tally_id):
    form = (
        db.session.query(Questionnaire)
        .filter_by(tally_id_questionnaire=tally_id)
        .first()
    )
    if not form:
        return None

    return form


def get_forms():
    questionnaires = db.session.query(Questionnaire).all()
    if not questionnaires:
        return None

    return questionnaires
