from typing import Dict, List, Type
from src.data.repositories import ProductRepositoryInterface
from src.domain.user_case import ProductUseCaseInterface


class FindProduct:
    """ Class to define use case: Find Product """
    def __init__(self, product_repository: Type[ProductRepository]):
        self.product_repository = product_repository

    def by_product_id(self, product_id: int) -> Dict[bool, List[Product]]:
        """Select Product By product_id
        :param - product_id: id of the product
        :return - Dictionary with information about the process
        """
        response = None
        validate_entry = isinstance(product_id, int)
        if validate_entry:
            response = self.product_repository.select_product(product_id=product_id)
        return {"Success": validate_entry, "Data": response}
    