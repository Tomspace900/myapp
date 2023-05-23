from sqlalchemy import Column, Integer, String, Boolean
from configs.db_config import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tally_id = Column(Integer)
    first_name = Column(String(255))
    last_name = Column(String(255))
    isAdmin = Column(Boolean)

    def __init__(self, tally_id, first_name, last_name, isAdmin):
        self.tally_id = tally_id
        self.first_name = first_name
        self.last_name = last_name
        self.isAdmin = isAdmin
