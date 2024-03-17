from uuid import uuid4
from sqlalchemy import Column, String, Float
from src.infrastructure.database.settings.base import Base


class Participant(Base):
    __tablename__ = "participant"

    id = Column(String, primary_key=True, autoincremant=True, default=uuid4)
    name = Column(String)
    value = Column(Float)
