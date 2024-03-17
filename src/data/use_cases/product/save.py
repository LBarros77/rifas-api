from typing import Dict, List, Type
from src.data.repositories import ProductRepositoryInterface
from src.domain.user_case import ProductUseCaseInterface


class SaveProduct:
    """ Class to define use case: Save Product """
    def __init__(self, product_repository: Type[ProductRepository]):
        self.product_repository = product_repository

    def create_product(self, product_data: Dict) -> Dict[bool, str]:
        """Create a new Product
        :param - product_data: dictionary containing product information
        :return - Dictionary with information about the process
        """
        response = None
        validate_entry = isinstance(product_data, dict)
        if validate_entry:
            response = self.product_repository.create_product(product_data)
        return {"Success": validate_entry, "Message": response}

    def update_product(self, product_id: int, updated_data: Dict) -> Dict[bool, str]:
        """Update an existing Product
        :param - product_id: id of the product to be updated
        :param - updated_data: dictionary containing updated product information
        :return - Dictionary with information about the process
        """
        response = None
        validate_entry = isinstance(product_id, int) and isinstance(updated_data, dict)
        if validate_entry:
            response = self.product_repository.update_product(product_id, updated_data)
        return {"Success": validate_entry, "Message": response}

    def delete_product(self, product_id: int) -> Dict[bool, str]:
        """Delete an existing Product
        :param - product_id: id of the product to be deleted
        :return - Dictionary with information about the process
        """
        response = None
        validate_entry = isinstance(product_id, int)
        if validate_entry:
            response = self.product_repository.delete_product(product_id)
        return {"Success": validate_entry, "Message": response}
