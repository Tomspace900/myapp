from configs.db_config import db
from models.form_model import Questionnaire
from services.user_service import create_user
from services.response_service import create_response, get_response, get_response_value
from services.question_service import create_question, get_question
from services.own_service import create_own, get_own
from services.result_service import create_result, get_result
from formatters.csv_formatter import format_csv
from datetime import datetime


def save_questionnaire(data):
    response_data = data[0]["data"]
    form_name = response_data["formName"]
    tally_id = response_data["formId"]
    user_tally_id = response_data["respondentId"]
    response_tally_id = response_data["responseId"]
    submission_date = response_data["createdAt"]
    questions = response_data["fields"]

    # Create user
    user = create_user(user_tally_id, False)

    # Create form
    questionnaire = create_questionnaire(tally_id, form_name)

    # Create response (submission)
    response = get_response(response_tally_id)
    
    if not response:
        response = create_response(
        response_tally_id, questionnaire.id_questionnaire, user.id_user, submission_date
    )

    # Create values to questions
    for q in questions:
        # Takes the last 6 characters which is the tally id
        question_tally_id = q["key"][-6:]
        
        # Get question from database
        question = get_question(question_tally_id)
        
        # If question does not already exist, create it
        if not question:
            print("question does not exist")
            question = create_question(q, questionnaire.id_questionnaire)
        
        print("question: ", question)
        
        # Link question to form
        association = get_own(questionnaire.id_questionnaire, question.id_question)
        
        if not association:
            create_own(questionnaire.id_questionnaire, question.id_question)
        
        # Get response value depending on question type
        response_value = get_response_value(q)

        result = get_result(response.id_response, question.id_question)
        
        print("response_id: ", response.id_response, "question_id: ", question.id_question, "value: ", response_value)
        
        if not result: 
            print("value does not exist")
            result = create_result(response.id_response, question.id_question, response_value)
        
        print("result: ", result)

    return questionnaire


def create_questionnaire(tally_id, form_name):
    # Check if questionnaire already exists
    existing_form = (
        db.session.query(Questionnaire)
        .filter_by(tally_id_questionnaire=tally_id)
        .first()
    )
    if existing_form:
        return existing_form
    
    now = datetime.now()

    questionnaire = Questionnaire(tally_id=tally_id, name=form_name, date_creation=now )

    # Add questionnaire to database
    db.session.add(questionnaire)
    db.session.commit()
    return questionnaire


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
        print("no questionnaires in database")
        return Exception("No questionnaires in database")
    
    print(len(questionnaires), "questionnaire(s) in database")

    return questionnaires

def get_csv():
    
    get_forms()

    file = format_csv()
    
    print("file: ", file)

    return file