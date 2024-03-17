from abc import ABC, abstractmethod
from src.domain.models import ProductModel


class ProductRepositoryInterface:
    """ product Repository Interface """
	@abstractmethod
	def find_by_id(self, product_id: str) -> List[ProductModel]:
		""" Find product by id
		:param - product_id is the product id
		:return - The return is a Product
		"""
		Exception("Should be needed implament find_by_id")

    @abstractmethod
    def save(self, product: ProductModel) -> None:
        """ Method to Save Product
		:param - product is object of type Produt
		"""
		Exception("Should be needed implament find_by_id")
