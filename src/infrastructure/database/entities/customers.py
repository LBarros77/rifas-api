from datetime import datetime
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped


class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    telephone = Column(String)
    email = Column(String, nullable=True)
    cpf = Column(String, nullable=True)
    timestamps: Mapped[datetime]
