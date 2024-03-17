from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped
from src.infrastructure.database.settings.base import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    link = Column(String)
    timestamps: Mapped[datetime]
