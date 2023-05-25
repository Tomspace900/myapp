from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from services.form_service import save_form

webhook = Blueprint("webhook", __name__)


# Webhook endpoint to save data : https://my-tally.thomasgendron.fr/form (POST)
@webhook.route("/", methods=["POST"])
def handleWebhook():
    data = request.get_json()
    save_form(data)
    return "OK", 200
