import pytest
import random
from datetime import datetime, timezone
from sqlalchemy import text
from faker import Faker
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.infrastructure.database.repositories.product_repository import ProductRepository


faker = Faker(["pt_BR", "en_US", "es_SP"])
db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

def test_add_product():
    ''' Should add a product '''

    start_date = datetime.date(2000, 1,1)
    end_date = datetime.date(2015, 1,1)
    mocked_id = random.randrange(1, 100)
    mocked_name = faker.name()
    mocked_price = 3.80
    mocked_status = random.choice(["pago", "pendente", "não pago"])
    mocked_quantity = faker.number()
    mocked_processed = faker.number()
    mocked_type_raffles = "desconhecido"
    mocked_favorite = False
    mocked_game_mode = "números"
    mocked_minimum = 2
    mocked_maximum = 1000
    mocked_user_id = "b5163063-f94e-4e70-ad42-06065fa7e3c7"
    mocked_draw_date = faker.date_time_between(start_date, end_date) # "2024-3-11 08:43:21"
    mocked_created_at = datetime.fromtimestamp(_timestamp(), tz=timezone.utc)

    product_repository = ProductRepository()
    product_repository.add_product(
        mocked_id,
        mocked_name,
        mocked_price,
        mocked_status,
        mocked_quantity,
        mocked_processed,
        mocked_type_raffles,
        mocked_favorite,
        mocked_game_mode,
        mocked_minimum,
        mocked_maximum,
        mocked_user_id,
        mocked_draw_date,
        mocked_created_at
    )

    sql = '''
        SELECT * FROM "Products"
        WHERE id = '{}'
        AND name = '{}';
    '''.format(mocked_id, mocked_name)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.id == mocked_id
    assert registry.name == mocked_name

    connection.commit()


def test_get_by_id():
    ''' Should get one product by id '''

    mocked_id = 1
    product_repository = ProductRepository()
    registry = product_repository.get_by_id(mocked_id)

    assert registry.id == mocked_id


def test_update():
    ''' Should be updation of elements in product '''

    mocked_id = 1
    mocked_attribuilts = {"quantity": faker.number(), "numbers": faker.number()}

    product_repository = ProductRepository()
    product_repository.update(mocked_id, mocked_attribuilts)

    sql = f'''SELECT quantity, numbers from "Product" WHERE id = '{mocked_id}';'''
    response = connection.excute(text(sql))
    registry = response.fetchall()[0]

    assert registry.quantity == mocked_attribuilts["quantity"]
    assert registry.numbers == mocked_attribuilts["numbers"]

    connection.commit()


def _timestamp() -> datetime:
    return datetime.now().timestamp()
