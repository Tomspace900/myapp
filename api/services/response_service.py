from api.configs.db_config import db
from api.models.response_model import Response
from api.models.values_model import Value


def create_response(questionnaire_id, user_id, submission_date):
    response = Response(
        questionnaire_id=questionnaire_id,
        user_id=user_id,
        submission_date=submission_date,
    )

    # Add response to database
    db.session.add(response)
    db.session.commit()
    return response


def get_response(response_id):
    response = Response.query.get(response_id)
    if not response:
        return None

    return response


def get_responses():
    responses = Response.query.all()
    if not responses:
        return None

    return responses
