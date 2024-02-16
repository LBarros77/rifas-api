from sqlalchemy import Column, Integer, String, required
from src.infrastructure.database.settings.base import Base


class Product(Base):
  __tablename__ = "products"

  id = Column(Integer, primary_key=True, autoincrement=True)
  numbers = Column(Integer, required)
  affiliate_earning = Column(Integer)

  def __repr__(self):
      return f"with {self.numbers} products affiliate earning: {self.affiliate_earning}"
