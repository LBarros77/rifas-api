from typing import Type, Dict
from src.data.interfaces import AffiliateSolicitationRepositoryInterface
from src.infrastructure.database.entities import AffiliateSolicitation


class AffiliateSolicitationUseCase:
	""" Class to define usecases: Affiliate solicitation """
	def __init__(self, affiliate_solicitation_repository: AffiliateSolicitationRepositoryInterface):
	    self.affiliate_solicitation_repository = affiliate_solicitation_repository

	def find_by_id(self, solicitation_id: int) -> Dict[str, str]:
		"""Find Affiliate solicitation by solicitation id
		:param - solicitation_id: id of the Affiliate solicitation
		:return - Dictionary with status of the process and data if success
		"""
		response = None
		validate_entry = isinstance(solicitation_id, int)
		if validate_entry:
			solicitation_obj = self.affiliate_solicitation_repository.find_by_id(solicitation_id)
			if solicitation_obj:
				response = {
					"status": "Success",
					"data": {
						"id": solicitation_obj.id,
						"affiliate_nome": solicitation_obj.affiliate.name,
						"total_valor": solicitation_obj.payed,
						"status": solicitation_obj.affiliate.status
					}
				}
			else:
				response = {"status": "Error", "data": "Affiliate solicitation not found"}
		return response
