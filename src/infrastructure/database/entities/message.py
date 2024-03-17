from sqlalchemy import Column, String
from src.infrastructure.database.settings.base import Base


class Message(Base):
    title = Column(String)
    body = Column(String)
