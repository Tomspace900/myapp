from configs.db_config import db
from models.value_model import Value


def create_value(id_question, id_response, value):
    value = Value(
        id_question=id_question,
        id_response=id_response,
        results=value,
    )

    # Add value to database
    db.session.add(value)
    db.session.commit()
    return value


def get_values_by_response_id(response_id):
    values = db.session.query(Value).filter_by(id_response=response_id).all()
    if not values:
        return None

    return values


def get_values_by_question_id(question_id):
    values = db.session.query(Value).filter_by(id_question=question_id).all()
    if not values:
        return None

    return values


def get_value(response_id, question_id):
    value = (
        db.session.query(Value)
        .filter_by(id_response=response_id, id_question=question_id)
        .first()
    )
    if not value:
        return None

    return value
