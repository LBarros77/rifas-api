from sqlalchemy import Column, String, ForeignKey, relationship
from src.infrastructure.database.settings.base import base


class PaymentPix(Base):
    __tablename__ = "payment_pix"

    id = Column(Integer, primary_key=True, autoincrement=True)
    key_pix = Column(String, nullable=False)
    participant_id = Column(Integer, ForeignKey("Participate.id"))

    participant = relationship("Participate", uselist=False, back_populates="payment_pix")
