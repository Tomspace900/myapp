from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from services.form_service import save_questionnaire

webhook = Blueprint("webhook", __name__)


# Webhook endpoint to save data
@webhook.route("/", methods=["POST"])
def handleWebhook():
    data = request.get_json()
    response = save_questionnaire(data)
    print(response)
    return "OK", 200
    # return jsonify(response), 200
