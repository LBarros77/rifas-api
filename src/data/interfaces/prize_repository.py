from abc import ABC, abstractmethod
from typing import List
from src.domain.models import PrizeModel as Prize


class PrizeRepositoryInterface(ABC):
	""" Prize Repository Interface """
	@abstractmethod
	def find_by_id(self, prize_id: str) -> List[Prize]:
		""" Find Prize by id
		:param - prize_id is the Prize id
		:return - The return is a Prize
		"""
		Exception("Should be needed implament find_by_id")
