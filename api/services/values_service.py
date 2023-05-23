from configs.db_config import session
from models.values_model import Value


def create_value(tally_id, response_id, question_id, value):
    value = Value(
        tally_id=tally_id,
        response_id=response_id,
        question_id=question_id,
        value=value,
    )

    # Add value to database
    session.add(value)
    session.commit()
    return value


def get_values_by_response_id(response_id):
    values = session.query(Value).filter_by(response_id=response_id).all()
    if not values:
        return None

    return values


def get_values_by_question_id(question_id):
    values = session.query(Value).filter_by(question_id=question_id).all()
    if not values:
        return None

    return values


def get_value(response_id, question_id):
    value = (
        session.query(Value)
        .filter_by(response_id=response_id, question_id=question_id)
        .first()
    )
    if not value:
        return None

    return value
