from sqlalchemy import Column, Integer, String
from src.infrastructure.database.settings.base import Base


class Participant(Base):
    __tablename__ = "participant"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numbers = Column(Integer)
    reserveds = Column(Integer)
    payeds = Column(Integer)
    confereds = Column(Integer)
