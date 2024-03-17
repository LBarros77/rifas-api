import datetime
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    type_anotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True)
    }
