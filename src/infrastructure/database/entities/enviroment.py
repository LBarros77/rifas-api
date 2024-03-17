from sqlalchemy import Column, String
from src.infrastructure.database.settings.base import base


class Enviroment(Base):
    __tablename__ = "consulting_enviroments"

    token_api_wpp = Column(String)
