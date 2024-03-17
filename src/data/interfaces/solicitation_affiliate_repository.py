from abc import ABC, abstractmethod
from src.domain.models import SolicitationAffiliateModel as SolicitationAffiliate


class SolicitationAffiliateRepositoryInterface(ABC):
	""" Cass to define Interface: Repository of Solicitation Affiliate """
	@abstractmethod
	def find_by_id(self, solicitation_id: str) -> SolicitationAffiliate:
		""" Method to find solicitaion by id
		:param - solicitation_id: id of the solicitation Affiliate
		:return - Object of Solicitation Affiliate
		"""
		Exception("Should needed implement the method find_by_id")