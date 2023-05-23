from api.configs.db_config import db
from api.models.user_model import User


def create_user(tally_id, first_name, last_name, isAdmin):
    # Check if user already exists
    existing_user = User.query.filter_by(tally_id=tally_id).first()
    if existing_user:
        return existing_user

    user = User(
        tally_id=tally_id, first_name=first_name, last_name=last_name, isAdmin=isAdmin
    )

    # Add user to database
    db.session.add(user)
    db.session.commit()
    return user
