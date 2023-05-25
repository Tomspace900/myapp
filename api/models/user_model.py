from configs.db_config import db


class User(db.Model):
    __tablename__ = "Users"

    id_user = db.Column(db.Integer, primary_key=True)
    tally_id_user = db.Column(db.Integer)
    firstname_user = db.Column(db.String(50))
    lastname_user = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean)

    def __init__(self, tally_id, firstname, lastname, is_admin):
        self.tally_id_user = tally_id
        self.firstname_user = firstname
        self.lastname_user = lastname
        self.is_admin = is_admin


@property
def id(self):
    return self.id_user


def tally_id(self):
    return self.tally_id_user


def firstname(self):
    return self.firstname_user


def lastname(self):
    return self.lastname_user
