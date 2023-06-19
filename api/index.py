from flask import Flask, request, render_template, redirect, session
from controllers.form_controller import form
from controllers.webhook_controller import webhook
from configs.db_config import db, database_url
from models.user_model import User
from hashlib import sha256
import secrets

# initialize the flask app
app = Flask(__name__)

# configure the secret key
app.secret_key = secrets.token_hex(16)

# configure the mysql database connection
app.config["SQLALCHEMY_DATABASE_URI"] = database_url

# initialize the app with the database
db.init_app(app)

# register the blueprints
app.register_blueprint(form, url_prefix="/form")
app.register_blueprint(webhook, url_prefix="/form")


# Main page
@app.route("/")
def home():
    return render_template("index.html")


# -------------- login


# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Vérifier l'authentification dans la base de données
        user = User.query.filter_by(username_user=username).first()

        print("sha256", sha256(password.encode("utf-8")).hexdigest())
        if user and user.password_user == sha256(password.encode("utf-8")).hexdigest():
            if user.is_admin:
                session["username"] = username
                return redirect("/")

        return render_template("login.html", incorrect=True)

    return render_template("login.html", incorrect=False)


# Prevent access to pages without logging in
@app.before_request
def require_login():
    if (
        request.method == "GET"
        and request.path != "/login"
        and request.path != "/logout"
    ):
        if "username" not in session:
            return redirect("/login")


# Logout
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")


# -------------- login


if __name__ == "__main__":
    app.run()
