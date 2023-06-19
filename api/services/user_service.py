from configs.db_config import db
from models.user_model import User


def create_user(tally_id, isAdmin):
    # Check if user already exists
    existing_user = db.session.query(User).filter_by(tally_id_user=tally_id).first()
    if existing_user:
        return existing_user

    user = User(
        tally_id=tally_id,
        is_admin=isAdmin,
    )

    # Add user to database
    db.session.add(user)
    db.session.commit()
    return user


def update_user_firstname(user_id, firstname):
    user = db.session.query(User).filter_by(id_user=user_id).first()
    user.firstname_user = firstname
    db.session.commit()
    return user


def update_user_lastname(user_id, lastname):
    user = db.session.query(User).filter_by(id_user=user_id).first()
    user.lastname_user = lastname
    db.session.commit()
    return user


def update_user_email(user_id, email):
    user = db.session.query(User).filter_by(id_user=user_id).first()
    user.email_user = email
    db.session.commit()
    return user


def update_user_phone(user_id, phone):
    user = db.session.query(User).filter_by(id_user=user_id).first()
    user.phone_user = phone
    db.session.commit()
    return user
