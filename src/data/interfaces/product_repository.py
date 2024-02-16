from abc import ABC, abstractmethod
from typing import List, Integer, String
from src.domain.models.product import Product, Participant


class IProductRepository:

    @abstractmethod
    def get_numbers(self, game_mode: str) -> List: pass

    @abstractmethod
    def get_participants(self, product_id: int) -> List[Participant]: pass

    @abstractmethod
    def get_all_numbers(self) -> List: pass

    @abstractmethod
    def set_numbers(self, numbers_list: list) -> None: pass

    @abstractmethod
    def get_quantity_available_numbers(self) -> Integer: pass

    @abstractmethod
    def get_random_numbers(self, quantity: int) -> String: pass

    @abstractmethod
    def get_available_numbers(self) -> List: pass

    @abstractmethod
    def get_quantity_reserved_numbers(self) -> Integer: pass

    @abstractmethod
    def get_reserved_numbers(self) -> List[Integer]: pass

    @abstractmethod
    def get_quantity_payed_numbers(self) -> Integer: pass

    @abstractmethod
    def percentage(self) -> Integer: pass

    @abstractmethod
    def get_participants(self) -> List[Participant]: pass

    @abstractmethod
    def get_reserved_participants(self) -> List[Participant]: pass

    @abstractmethod
    def get_promotions(self) -> List: pass
