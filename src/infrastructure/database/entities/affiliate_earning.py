from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.infrastructure.database.settings.base import Base

class AffiliateEarning(Base):
    product_id = Column(Integer, ForeignKey("product_id"))
    participant_id = Column(String, ForeignKey("participant_id"))
    affiliate_id = Column(String, ForeignKey("affiliate_id"))
    solicitation_id = Column(Integer, ForeignKey("solicitation_id"))
    price = Column(Float)
    payed = Column(Float)

    product = relationship("Product", back_populates="affiliate_earning")
    participant = relationship("Participant", back_populates="affiliate_earning")
    affiliate = relationship("Affiliate", back_populates="affiliate_earning")
    solicitation = relationship("Solicitation", back_populates="affiliate_earning")
