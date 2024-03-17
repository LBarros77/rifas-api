# from typing import Literal
from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from src.infrastructure.database.settings.base import Base


# Status = Literal["disponível", "reservado", "pago"]

class Raffle(Base):
    __tablename__ = "Raffles"

    product_id = Column(Integer, ForeignKey("Products.id"), primary_key=True)
    participant_id = Column(String, ForeignKey("Participate.participant_id"), primary_key=True)

    product = relationship("Products")
    participate = relationship("Participate")

    __table_args__ = (UniqueConstraint("product_id", "participant_id"),)
