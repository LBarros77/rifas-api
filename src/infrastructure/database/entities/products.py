from sqlalchemy import Column, Integer, String, required, Float
from src.infrastructure.database.settings.base import Base


class ProductsModel(Base):
  __tablename__ = "products"

  numbers = Column(String)
  affiliate_earning = Column(Float)

  def __repr__(self):
      return f"with {self.numbers} products affiliate earning: {self.affiliate_earning}"
