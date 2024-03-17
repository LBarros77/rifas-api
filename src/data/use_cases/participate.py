from typing import List, Dict, Type
from src.data.interfaces import ParticipateRepositoryInterface
from src.domain.user_case import ParticipateUserCaseInterface


class ParticipateUseCase(ParticipateUserCaseInterface):
    def __init__(self, participate_repository: Type[ParticipateRepositoryInterface]):
        self.participate_repository = participate_repository

    def get_participate_reserveds(self, participate_id: int) -> Dict[str, List[int]]:
        """
        Get reserved numbers for a participant
        :param participate_id: The ID of the participant
        :return: A dictionary containing the reserved numbers
        """
        response = None
        validate_entry = isinstance(participate_id, int)
        if validate_entry:
            response = self.participate_repository.get_reserveds(participate_id)
        return {"Success": validate_entry, "Data": response}

    def get_participate_quantity_reserveds(self, participate_id: int) -> Dict[str, int]:
        """
        Get the quantity of reserved numbers for a participant
        :param participate_id: The ID of the participant
        :return: A dictionary containing the quantity of reserved numbers
        """
        response = None
        validate_entry = isinstance(participate_id, int)
        if validate_entry:
            response = self.participate_repository.get_reserveds_quantity(participate_id)
        return {"Success": validate_entry, "Data": response}

    def get_participate_status(self, participate_id: int) -> Dict[str, str]:
        """
        Get the status of a participant
        :param participate_id: The ID of the participant
        :return: A dictionary containing the status of the participant
        """
        response = None
        validate_entry = isinstance(participate_id, int)
        if validate_entry:
            response = self.participate_repository.status(participate_id)
        return {"Success": validate_entry, "Data": response}

    def get_participate_situation(self, participate_id: int) -> Dict[str, str]:
        """
        Get the situation of a participant
        :param participate_id: The ID of the participant
        :return: A dictionary containing the situation of the participant
        """
        response = None
        validate_entry = isinstance(participate_id, int)
        if validate_entry:
            response = self.participate_repository.get_situation(participate_id)
        return {"Success": validate_entry, "Data": response}

    def get_participate_pagos(self, participate_id: int) -> Dict[str, List[int]]:
        """
        Get paid numbers for a participant
        :param participate_id: The ID of the participant
        :return: A dictionary containing the paid numbers
        """
        response = None
        validate_entry = isinstance(participate_id, int)
        if validate_entry:
            response = self.participate_repository.get_participate_pagos(participate_id)
        return {"Success": validate_entry, "Data": response}
