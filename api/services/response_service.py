from configs.db_config import session
from models.response_model import Response


def create_response(questionnaire_id, user_id, submission_date):
    response = Response(
        questionnaire_id=questionnaire_id,
        user_id=user_id,
        submission_date=submission_date,
    )

    # Add response to database
    session.add(response)
    session.commit()
    return response


def get_response(response_id):
    response = session.query(Response).filter_by(id=response_id).first()
    if not response:
        return None

    return response


def get_responses():
    responses = session.query(Response).all()
    if not responses:
        return None

    return responses
