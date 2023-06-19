from configs.db_config import db
from models.result_model import Result
from models.question_model import Question
from models.response_model import Response
from services.user_service import (
    update_user_firstname,
    update_user_lastname,
    update_user_email,
    update_user_phone,
)


def create_result(id_response, id_question, value):
    print("id_question: ", id_question, "id_response: ", id_response, "value: ", value)
    value = Result(
        id_question=id_question,
        id_response=id_response,
        results=value,
    )

    if value.results:
        is_key_question(id_question, id_response, value.results)

    # Add value to database
    db.session.add(value)
    db.session.commit()
    return value


def is_key_question(id_question, id_response, value):
    # get question label
    question = db.session.query(Question).filter_by(id_question=id_question).first()
    response = db.session.query(Response).filter_by(id_response=id_response).first()
    label = question.label_question
    type = question.type_question
    user_id = response.id_user

    # check if label contains "nom" or "prénom"
    if "prenom" in label.lower() or "prénom" in label.lower():
        update_user_firstname(user_id, value)
        print("firstname of user", user_id, "updated to", value)
        return True
    elif "nom" in label.lower():
        update_user_lastname(user_id, value)
        print("lastname of user", user_id, "updated to", value)
        return True
    elif type == "INPUT_EMAIL":
        update_user_email(user_id, value)
        print("email of user", user_id, "updated to", value)
        return True
    elif type == "INPUT_PHONE_NUMBER":
        update_user_phone(user_id, value)
        print("phone of user", user_id, "updated to", value)
        return True


def get_results_by_response_id(response_id):
    values = db.session.query(Result).filter_by(id_response=response_id).all()
    if not values:
        return None

    return values


def get_results_by_question_id(question_id):
    values = db.session.query(Result).filter_by(id_question=question_id).all()
    if not values:
        return None

    return values


def get_result(response_id, question_id):
    value = (
        db.session.query(Result)
        .filter_by(id_response=response_id, id_question=question_id)
        .first()
    )
    if not value:
        return None

    return value
