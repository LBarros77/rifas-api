from typing import List, Dic
from decimal import Decimal
from datetime import datetime
from sqlalchemy import update
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.infrastructure.database.entities.product import Product
from src.data.interfaces.product_repository import IProductRepository
from src.domain.models.product import ProductModel


class ProductRepository(IProductRepository):
    """ Class to define Repository: Product """
    @classmethod
    def add_product(
        cls,
        id: int,
        name: str,
        price: Decimal,
        status: str,
        quantity: int,
        processed: int,
        type_raffles: str,
        favorite: bool,
        game_mode: str,
        minimum: int,
        maximum: int,
        user_id: str,
        draw_date: datetime,
        created_at: datetime
    ) -> None:
        with DBConnectionHandler() as database:
            try:
                product = Product(
                    id=id,
                    name=name,
                    price=price,
                    status=status,
                    quantity=quantity,
                    processed=processed,
                    type_raffles=type_raffles,
                    favorite=favorite,
                    game_mode=game_mode,
                    minimum=minimum,
                    maximum=maximum,
                    user_id=user_id,
                    draw_date=draw_date,
                    created_at=created_at
                )
                database.session.add(product)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def get_by_id(cls, product_id: int) -> ProductModel:
        with DBConnectionHandler() as database:
            try:
                product = database.session.get(Product, product_id)
                return product
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update(cls, product_id, elements: Dic) -> str:
        with DBConnectionHandler() as database:
            try:
                database.session
                    .get(Product, product_id)
                    .update(elements)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_raffles(cls) -> List[Raffle]:
        with DBConnectionHandler() as database:
            try:
                raffles = database.session.query(Product)
                    .join(Raffle, Product.id == Raffle.product_id)
                    .with_entities(Product.id)
                    .all()
                return raffles
            except Exception as exception:
                database.session.rollback()
                raise exception


'''
class ProductRepository(IProductRepository):

    @classmethod
    def add_product(
        cls,
        game_mode: str,
        numbers: int,
        qtd: int,
        qtd_ranking: int,
        draw_date: str,
        status: str,
        affiliate_earning: int
    ) -> None:
        with DBConnectionHandler() as database:
            try:
                product = Product(
                    game_mode=game_mode,
                    numbers=numbers,
                    qtd=qtd,
                    qtd_ranking
                    draw_date
                    status
                    affiliate_earning=affiliate_earning
                )
                database.session.add(product)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def get_numbers(cls, game_mode: str) -> List:
        with DBConnectionHandler() as database:
            try:
                # find affiliate numbers
                product = database.session
                    .query(ProductEntity)
                    .filter(ProductEntity.game_mode == game_mode)
                numbers = product.numbers.split(",")
                return numbers
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def get_participants(cls, product_id: int) -> List[Participant]: pass

    @classmethod
    def get_all_numbers(cls) -> List: pass

    @classmethod
    def set_numbers(cls, numbers_list: list) -> None: pass

    @classmethod
    def get_quantity_available_numbers(cls) -> Integer: pass

    @classmethod
    def get_random_numbers(cls, quantity: int) -> String: pass

    @classmethod
    def get_available_numbers(cls) -> List: pass

    @classmethod
    def get_quantity_reserved_numbers(cls) -> Integer: pass

    @classmethod
    def get_reserved_numbers(cls) -> List[Integer]: pass

    @classmethod
    def get_quantity_payed_numbers(cls) -> Integer: pass

    @classmethod
    def percentage(cls) -> Integer: pass

    @classmethod
    def get_participants(cls) -> List[Participant]: pass

    @classmethod
    def get_reserved_participants(cls) -> List[Participant]: pass

    @classmethod
    def get_promotions(cls) -> List: pass

    @classmethod
    def save(cls, product_entity: ProductEntity):
        with DBConnectionHandler() as database:
            product = cls._map_to_model(product_entity)
            try:
                database.session.add(product)
                database.session.commit()
            except SQLAlchemyError as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def _map_to_model(model, entity: ProductEntity) -> ProductEntity:
        model = Product(
            id=entity.id,
            numbers=entity.numbers,
            affiliate_earning=entity.affiliate_earning
        )
        return model
'''
