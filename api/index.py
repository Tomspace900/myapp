from flask import Flask, request, jsonify, render_template, redirect, url_for
from controllers.form_controller import form
from controllers.webhook_controller import webhook
from configs.db_config import db, database_url


# initialize the flask app
app = Flask(__name__)

# configure the mysql database connection
app.config["SQLALCHEMY_DATABASE_URI"] = database_url

# initialize the app with the database
db.init_app(app)

# register the blueprints
app.register_blueprint(form, url_prefix="/form")
app.register_blueprint(webhook, url_prefix="/form")

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
