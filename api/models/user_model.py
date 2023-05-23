from api.configs.db_config import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    tally_id = db.Column(db.Integer)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    isAdmin = db.Column(db.Boolean)

    def __init__(self, tally_id, first_name, last_name, isAdmin):
        self.tally_id = tally_id
        self.first_name = first_name
        self.last_name = last_name
        self.isAdmin = isAdmin
