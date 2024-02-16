from typing import List
from uuid import uuid4
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.infrastructure.database.entities.user import User as UserEntity
from src.data.interfaces.user_repository import IUserRepository


class UserRepository(IUserRepository):

    @classmethod
    def add_user(
        cls,
        name: str,
        phone_number: str,
        status: bool,
        email: str,
        password: str,
        cpf: str,
        pix: str,
        affiliate: bool,
        remember_token: str,
        timestamps: str
    ) -> None:
        with DBConnectionHandler() as database:
            try:
                user = UserEntity(
                    id=uuid4(),
                    name=name,
                    phone_number=phone_number,
                    status=status,
                    email=email,
                    password=password,
                    cpf=cpf,
                    pix=pix,
                    affiliate=affiliate,
                    remember_token=remember_token,
                    timestamps=timestamps
                )
                database.session.add(user)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def delete_user(cls, user_id: str) -> None:
        with DBConnectionHandler() as database:
            try:
                database.session.query(UserEntity).filter_by(id=user_id).delete()
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception


    #@classmethod
    #def total_gain(cls) -> int:
    #    if cls.affiliate is False: return 0
    #    with DBConnectionHandler as database:
    #        try:
    #            affiliates = database.session
    #                .query(UserEntity)
    #                .find_by(id == AffiliateEntity.id)
    #                .all()
    #            values = affiliates.values()
    #            total_gain = sum(values)
    #            return total_gain
    #        except Exception as exception:
    #            database.session.rollback()
    #            raise exception
