from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infrastructure.database.settings.base import Base

class Raffle(Base):
    __tablename__ = "raffles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String)
    product_id = Column(Integer)
    participant_id = Column(Integer)
    status = Column(String)
