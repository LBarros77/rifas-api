from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, relationship
from sqlalchemy.orm import Mapped
from src.infrastructure.database.base import Base


class AffiliateSolicitation(Base):
    """ Class define entity: Affiliate Solicitation """ 
    __tablename__ = "affiliate solicitation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    affiliate_id = Column(String, ForeignKey('users.id'), nullable=True)
    payed = Column(Boolean, default=False)
    timestamps = Mapped[datetime]

    affiliate = relationship("Users", backref="Users", layer=True)
