from datetime import datetime
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped

class AutoMessage(Base):
    __tablename__ = "auto_messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    identificador = Column(String)
    descricao = Column(String)
    destinatario = Column(String)
    msg = Column(Text, default='')
    timestamps: Mapped[datetime]
