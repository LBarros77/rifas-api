from abc import ABC, abstractmethod
from src.domain.models import ParticipantModel


class ParticipateRepositoryInterface(ABC):
  """ Participate Repository Interface """
  @abstractmethod
	def find_by_id(self, participant_id: str) -> ParticipantModel:
		""" Find Participant by id
		:param - participant_id is the participant id
		:return - The return is a Participant
		"""
		Exception("Should be needed implament find_by_id")