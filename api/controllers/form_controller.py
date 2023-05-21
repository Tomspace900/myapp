from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from api.services.form_service import save_form, get_forms

form = Blueprint("form", __name__)


@form.route("/", methods=["GET"])
def get_data():
    return get_forms()


# Webhook endpoint to save data : https://my-tally.thomasgendron.fr/form/webhook
@form.route("/webhook", methods=["POST"])
def handleWebhook():
    data = request.get_json()
    save_form(data)
    return "OK", 200
