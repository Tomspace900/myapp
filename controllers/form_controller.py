from flask import Blueprint, send_file, render_template
from services.form_service import get_forms, get_csv
import os
import csv
from dotenv import load_dotenv

# load environment variables
load_dotenv()
file_path = os.getenv("CSV_PATH")

form = Blueprint("form", __name__)


@form.route("/", methods=["GET"])
def get_forms():
    print("get_forms() called")
    get_forms()
    return "OK", 200


@form.route("/csv", methods=["GET"])
def get_csv_data():
    print("get_csv_data() called")
    data = get_csv()
    print("data:", data)
    return data, 200


@form.route("/csv/table", methods=["GET"])
def get_data_table():
    print("get_data_table() called")
    get_csv()
    with open(file_path) as csvfile:
        data = csv.reader(csvfile, delimiter=";")
        headers = next(data)
        return render_template("data.html", headers=headers, data=data)


@form.route("/csv/download", methods=["GET"])
def dl_csv_data():
    print("dl_csv_data() called")
    get_csv()
    path = "../" + file_path
    return send_file(
        path,
        as_attachment=True,
        download_name="data.csv",
        mimetype="text/csv",
    )
