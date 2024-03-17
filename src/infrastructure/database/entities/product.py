from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.types import DateTime, DECIMAL
from sqlalchemy.orm import relationship
from src.infrastructure.database.settings.base import Base


class Product(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String)
    price = Column(DECIMAL)
    status = Column(String, nullable=True)
    quantity = Column(Integer, default=1)
    processed = Column(Integer, default=0)
    type_raffles = Column(String)
    favorite = Column(Boolean, default=False)
    game_mode = Column(String)
    numbers = column(String)
    minimum = Column(Integer)
    maximum = Column(Integer)
    user_id = Column(String, ForeignKey("Users.id"))
    draw_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime)

    # user = relationship("Users")
    raffle = relationship("Raffles", backref="Raffles")
