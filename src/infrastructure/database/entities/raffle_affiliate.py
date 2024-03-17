from datetime import datetime
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped, relationship
from src.infrastructure.database.settings.base import Base


class RaffleAffiliate(Base):
    __tablename__ = "reffle_affiliates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('Products.id'), nullable=True)
    afiliado_id = Column(Integer, ForeignKey('Users.id'), nullable=True)
    token = Column(String)
    timestamps: Mapped[datetime]

    product = relationship("Products")
    afiliado = relationship("Users")
