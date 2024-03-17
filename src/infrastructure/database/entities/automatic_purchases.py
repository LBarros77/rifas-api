from datetime import datetime
from sqlalchemy import Column, Integer, Boolean, DateTime, relationship
from sqlalchemy.orm import Mapped
from src.infrastructure.database.settings.base import Base

class AutomaticPurchases(Base):
    __tablename__ = "compras_automaticas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    popular = Column(Boolean, default=False)
    timestamps: Mapped[datetime]

    product = relationship("Products")
