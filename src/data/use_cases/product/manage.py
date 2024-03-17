from typing import Dict, List, Type
from src.data.repositories import ProductRepositoryInterface
from src.domain.user_case import ProductUseCaseInterface

class ProductUseCase(ProductUseCaseInterface):
    def __init__(self, product_repository: Type[ProductRepositoryInterface]):
        self.product_repository = product_repository

    def get_numbers(self, product_id: int) -> Dict[str, List[str]]:
        response = None
        validate_entry = isinstance(product_id, int)
        if validate_entry:
            response = self.product_repository.get_numbers(product_id)
        return {"Success": validate_entry, "Data": response}

    def get_participants_array(self, product_id: int, limit: int) -> Dict[str, str]:
        response = None
        validate_entry = isinstance(product_id, int) and isinstance(limit, int)
        if validate_entry:
            response = self.product_repository.get_participants_array(product_id, limit)
        return {"Success": validate_entry, "Data": response}

    def save_numbers(self, product_id: int, numbers_array: List[int]) -> Dict[bool, str]:
        """Save numbers for a product
        :param - product_id: id of the product
        :param - numbers_array: list of numbers to be saved
        :return - Dictionary with information about the process
        """
        response = None
        validate_entry = isinstance(product_id, int) and isinstance(numbers_array, list)
        if validate_entry:
            response = self.product_repository.save_numbers(product_id, numbers_array)
        return {"Success": validate_entry, "Message": response}

    def numbers(self, product_id: int) -> List[str]:
        ''' Identify if game mode is numbers and return a list of this numbers else return id from product relationed to raffle '''
        product = self.product_repository.get_by_id(product_id)
        if product.game_mode is "números":
            return product.numbers
        return product.raffle.product_id
