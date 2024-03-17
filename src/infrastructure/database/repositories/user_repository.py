from typing import List
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.infrastructure.database.entities import User
from src.data.interfaces.user_repository import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    """ Class to define Repository: User """
    @classmethod
    def add_user(
        cls,
        id: str,
        name: str,
        phone_number: str,
        status: bool,
        email: str,
        password: str,
        cpf: str,
        pix: str,
        affiliate: bool,
        remember_token: str,
        created_at: str
    ) -> None:
        with DBConnectionHandler() as database:
            try:
                user = User(
                    id=id,
                    name=name,
                    phone_number=phone_number,
                    status=status,
                    email=email,
                    password=password,
                    cpf=cpf,
                    pix=pix,
                    affiliate=affiliate,
                    remember_token=remember_token,
                    created_at=created_at
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
                database.session.query(User).filter_by(id=user_id).delete()
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
