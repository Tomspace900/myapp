from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from services.form_service import get_forms

form = Blueprint("form", __name__)


@form.route("/", methods=["GET"])
def get_data():
    return get_forms()
