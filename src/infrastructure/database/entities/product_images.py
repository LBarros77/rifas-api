from datetime import datetime
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped


class ProductsImages(Base):
    __tablename__ = "products_images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    product_id = Column(Integer, ForeignKey('products.id'))
    timestamps: Mapped[datetime]

    product = relationship("Products")
