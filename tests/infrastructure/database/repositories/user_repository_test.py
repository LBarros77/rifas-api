import pytest
from datetime import datetime
from sqlalchemy import text
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.infrastructure.database.repositories.user_repository import UserRepository


db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

def test_add_user():
    mocked_name = "Joe Doe"
    mocked_phone_number = "31996676234"
    mocked_status = True
    mocked_email = "joe@company.com"
    mocked_password = "password"
    mocked_cpf = "10349037814"
    mocked_pix = "pix-key"
    mocked_affiliate = True
    mocked_remember_token = "dsfkmglregkv"
    mocked_timestamps = datetime.now()

    user_repository = UserRepository()
    user_repository.add_user(
        mocked_name,
        mocked_phone_number,
        mocked_status,
        mocked_email,
        mocked_password,
        mocked_cpf,
        mocked_pix,
        mocked_affiliate,
        mocked_remember_token,
        mocked_timestamps
    )

    sql = '''
        SELECT * FROM users
        WHERE name = '{}'
        AND email = '{}'
    '''.format(mocked_name, mocked_email)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.name == mocked_name
    assert registry.email == mocked_email

    connection.execute(text(f'''
        DELETE FROM users WHERE id = '{registry.id}'
    '''))
    connection.commit()


def test_delete_user():
    user_repository = UserRepository()
    mocked_id = "9rfvGL08-gfgk5486-0348dg"
    user_repository.delete_user(mocked_id)
    user_id = connection.execute(text(f'''
        SELECT id FROM users WHERE id = '{mocked_id}'
    '''))
    assert mocked_id is not user_id
