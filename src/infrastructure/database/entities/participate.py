from typing import List
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.database.settings.base import Base


class Participate(Base):
    __tablename__ = "Participate"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numbers = Column(String)
    reserveds = Column(Integer)
    payeds = Column(Integer)
    conferred = Column(Boolean, default=True)

    product = relationship('Products', uselist=False, back_populates='participant')
    order = relationship('Orders', uselist=False, back_populates='participant')
    raffle = relationship('Raffles', back_populates='participant')
    payment_pix = relationship('PaymentPix', uselist=False, back_populates='participant')
