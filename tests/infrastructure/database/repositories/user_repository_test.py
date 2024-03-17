import pytest
from uuid import uuid4
from datetime import datetime, timezone
from sqlalchemy import text
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.infrastructure.database.repositories.user_repository import UserRepository


db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="sensitive test")
def test_add_user():
    timestamp = datetime.now().timestamp()
    mocked_id = uuid4()
    mocked_name = "Demo Demo"
    mocked_phone_number = "31996676234"
    mocked_status = True
    mocked_email = "demo@company.com"
    mocked_password = "password"
    mocked_cpf = "10349037814"
    mocked_pix = "pix-key"
    mocked_affiliate = True
    mocked_remember_token = "dsfkmglregkv"
    mocked_created_at = datetime.fromtimestamp(timestamp, tz=timezone.utc)

    user_repository = UserRepository()
    user_repository.add_user(
        mocked_id,
        mocked_name,
        mocked_phone_number,
        mocked_status,
        mocked_email,
        mocked_password,
        mocked_cpf,
        mocked_pix,
        mocked_affiliate,
        mocked_remember_token,
        mocked_created_at
    )

    sql = '''
        SELECT * FROM "Users"
        WHERE name = '{}'
        AND email = '{}';
    '''.format(mocked_name, mocked_email)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.name == mocked_name
    assert registry.email == mocked_email

    connection.commit()


@pytest.mark.skip(reason="sensitive test")
def test_delete_user():
    user_repository = UserRepository()
    mocked_id = "9rfvGL08-gfgk5486-0348dg"
    user_repository.delete_user(mocked_id)
    user_id = connection.execute(text(f'''
        SELECT id FROM "Users" WHERE id = '{mocked_id}';
    '''))
    assert mocked_id is not user_id
