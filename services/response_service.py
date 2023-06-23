from configs.db_config import db
from models.response_model import Response
from datetime import datetime


def create_response(tally_id_responses, questionnaire_id, user_id, submission_date):
    formatted_submission_date = datetime.strptime(
        submission_date, "%Y-%m-%dT%H:%M:%S.%fZ"
    )
    response = Response(
        tally_id=tally_id_responses,
        questionnaire_id=questionnaire_id,
        user_id=user_id,
        submission_date=formatted_submission_date,
    )

    # Add response to database
    db.session.add(response)
    db.session.commit()
    return response


def get_response(tally_id):
    response = db.session.query(Response).filter_by(tally_id_responses=tally_id).first()
    if not response:
        return None

    return response


def get_responses():
    responses = db.session.query(Response).all()
    if not responses:
        return None

    return responses


def get_response_value(question):
    question_type = question["type"]
    response_value = None

    # si il y a un champ 'options' dans la question, on récupère la valeur de l'option
    if question_type in ["DROPDOWN", "MULTIPLE_CHOICE"]:
        for option in question["options"]:
            if option["id"] == question["value"]:
                response_value = option["text"]
                break
    elif question_type in [
        "INPUT_TEXT",
        "INPUT_EMAIL",
        "INPUT_PHONE_NUMBER",
        "RATING",
        "LINEAR_SCALE",
    ]:
        response_value = question["value"]

    return response_value
