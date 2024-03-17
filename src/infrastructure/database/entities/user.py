from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.types import DateTime
from src.infrastructure.database.settings.base import Base


class User(Base):
    __tablename__ = "Users"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String(11), nullable=False)
    status = Column(Boolean, default=False)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    cpf = Column(String(15), unique=True)
    pix = Column(String)
    affiliate = Column(Boolean, default=False)
    remember_token = Column(String)
    created_at = Column(DateTime)

    def __repr__(self):
        return f"Users [id={self.id}, first_name={self.name}]"
