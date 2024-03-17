from typing import List
from sqlalchemy import Column, Mapped
from src.infrastructure.database.settings.base import Base


class AwardModel(Base):
    product_id = mapped_column(ForeignKey("product.id"))
    participant_id = mapped_column(ForeignKey("participate.participant_id"))
    order = Column(String)
    phone_number = Column(String)
    description = Column(String)
    winner = Column(String)
    quota = Column(String)
    photo = Column(String)

    product = relationship("Product", back_populates="product.id")
    participant = relationship("Participate", back_populates="participate.participant_id")
