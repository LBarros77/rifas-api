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
        SELECT * FROM user
        where name = {}
        AND email = {}
    '''.format(mocked_name, mocked_email)
    response = connection.execute(text(sql))
    register = response.fetchall()[0]

    assert register.name == mocked_name
    assert register.email == mocked_email

    connection.execute(text(f'''
        DELETE FROM user WHERE id = {register.id}
    '''))
    connection.commit()
