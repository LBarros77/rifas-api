from src.data.interfaces import AffiliateSolicitationReposiroryInterface
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.domain.models import AffiliateSolicitationModel
from src.infrastructure.database.entities import AffiliateSolicitation


class AffiliateSolicitationRepository(AffiliateSolicitationReposiroryInterface):
    """ Class to define Interface: Repository of Affiliate Solicitation """
	@classmethod
	def find_by_id(cls, solicitation_id: str) -> AffiliateSolicitationModel:
		""" Method to find solicitaion by id
		:param - solicitation_id: id of the Affiliate Solicitation
		:return - Object of Affiliate Solicitation
		"""
        with DBConnectionHandler() as database:
            try:
                affiliate_solicitation = database.session.get(AffiliateSolicitation, solicitation_id)
                return affiliate_solicitation
            except Exception as exception:
                database.session.rollback()
                raise exception