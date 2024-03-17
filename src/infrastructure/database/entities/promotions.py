from datetime import datetime
from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import Mapped, relationship
from src.infrastructure.database.settings.base import Base


class PromotionsModel(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numbers_quantity = Column(Integer, default=0)
    order = Column(Integer)
    price = Column(Float, default=0)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=True)
    discount = Column(Float, default=0)
    timestamps: Mapped[datetime]

    product = relationship("Products")
