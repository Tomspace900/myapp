from configs.db_config import db


class User(db.Model):
    __tablename__ = "Users"

    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tally_id_user = db.Column(db.String(6))
    firstname_user = db.Column(db.String(50))
    lastname_user = db.Column(db.String(50))
    email_user = db.Column(db.String(100))
    phone_user = db.Column(db.String(10))
    is_admin = db.Column(db.Boolean)
    username_user = db.Column(db.String(100), unique=True, nullable=False)
    password_user = db.Column(db.String(100))

    def __init__(self, tally_id, is_admin):
        self.tally_id_user = tally_id
        self.is_admin = is_admin
