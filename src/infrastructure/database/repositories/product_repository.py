from typing import List
from src.infrastructure.settings.connection import DBConnectionHandler
from src.infrastructure.database.entities.product import Product as ProductEntity
from src.data.interfaces.product_repository import IProductRepository
from src.domain.models.product import Product


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
                product = ProductEntity(
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
