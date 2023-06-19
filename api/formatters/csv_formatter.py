from configs.db_config import db
from models.own_model import Own
from models.question_model import Question
from models.response_model import Response
from models.result_model import Result
from models.user_model import User
from formatters.string_formatter import format_string
import csv
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()
file_path = os.getenv("CSV_PATH")


def format_csv():
    questions = db.session.query(Question).all()
    print(len(questions), "questions")

    responses = db.session.query(Response).all()
    print(len(responses), "responses")

    headers = format_headers(questions)
    print("headers:", headers)

    rows = []

    for response in responses:
        row = format_responses(response, questions)
        print("row:", row)
        rows.append(row)

    with open(file_path, "w", newline="") as csvfile:
        datawriter = csv.writer(csvfile, delimiter=";")
        datawriter.writerow(headers)
        for row in rows:
            datawriter.writerow(row)

    file = open(file_path, "r", encoding="utf-8")

    return file


def format_headers(questions):
    headers = ["date", "id_questionnaire", "id_user"]

    for question in questions:
        label = format_string(question.label_question)

        label = str(question.id_question) + "_" + label

        headers.append(label)

    return headers


def format_responses(response, questions):
    row = []

    row.append(response.date_soumission)
    row.append(response.id_questionnaire)
    row.append(response.id_user)

    for question in questions:
        result = (
            db.session.query(Result)
            .filter(
                Result.id_response == response.id_response,
                Result.id_question == question.id_question,
            )
            .first()
        )
        if result:
            row.append(result.results)
        else:
            row.append("")

    return row


# csv headers :
# date, id_questionnaire, id_user, label_question1, label_question2, label_question3, label_question4, label_question5, label_question6, etc..
