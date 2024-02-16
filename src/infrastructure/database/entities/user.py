from sqlalchemy import Column, String, Integer, Boolean, DateTime
from datetime import datetime
from src.infrastructure.database.settings.base import Base


class User(Base):
    __tablename__ = "users"

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
    timestamps = Column(DateTime, default=datetime.now(tz=None))

    def __repr__(self):
        return f"Users [id={self.id}, first_name={self.name}]"
