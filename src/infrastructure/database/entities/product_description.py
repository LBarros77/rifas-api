from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped

class ProductDescription(Base):
    __tablename__ = "product_description"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text)
    product_id = Column(Integer, ForeignKey('products.id'))
    video = Column(String, nullable=True)
    timestamps: Mapped[datetime]

    product = relationship("Products")
