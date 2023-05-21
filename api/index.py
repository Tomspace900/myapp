from flask import Flask, request, jsonify, render_template, redirect, url_for
from api.controllers.form_controller import form

app = Flask(__name__)

app.register_blueprint(form, url_prefix="/form")

stored_data = []


# Main page
@app.route("/")
def home():
    return render_template("index.html")


# Webhook endpoint
@app.route("/webhook", methods=["POST"])
def handleWebhook():
    data = request.get_json()
    stored_data.append(data)
    return "OK", 200


# Data visualization page
@app.route("/data")
def get_data():
    print(stored_data)
    # return jsonify(stored_data)
    return render_template("data.html", data=stored_data)


# Send data to the frontend (Tableau / Dataiku)
@app.route("/get-data", methods=["GET"])
def send_data():
    return jsonify(stored_data)


if __name__ == "__main__":
    app.run()
