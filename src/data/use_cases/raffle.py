from typing import Dict, List, Type
from src.data.repositories import RaffleRepositoryInterface
from src.domain.user_case import RaffleUseCaseInterface


class RaffleUseCase(RaffleUseCaseInterface):
    def __init__(self, raffle_repository: Type[RaffleRepositoryInterface]):
        self.raffle_repository = raffle_repository

    def get_raffle_status(self, raffle_id: int) -> Dict[str, str]:
        """
        Get the status of a raffle
        :param raffle_id: The ID of the raffle
        :return: A dictionary containing the status of the raffle
        """
        response = None
        validate_entry = isinstance(raffle_id, int)
        if validate_entry:
            response = self.raffle_repository.get_raffle_status(raffle_id)
        return {"Success": validate_entry, "Data": response}

    def get_raffle_group(self, raffle_id: int) -> Dict[str, str]:
        """
        Get the group of a raffle
        :param raffle_id: The ID of the raffle
        :return: A dictionary containing the group of the raffle
        """
        response = None
        validate_entry = isinstance(raffle_id, int)
        if validate_entry:
            response = self.raffle_repository.get_raffle_group(raffle_id)
        return {"Success": validate_entry, "Data": response}

    def get_raffle_group_side(self, raffle_id: int) -> Dict[str, str]:
        """
        Get the group side of a raffle
        :param raffle_id: The ID of the raffle
        :return: A dictionary containing the group side of the raffle
        """
        response = None
        validate_entry = isinstance(raffle_id, int)
        if validate_entry:
            response = self.raffle_repository.get_raffle_group_side(raffle_id)
        return {"Success": validate_entry, "Data": response}

    def get_raffle_numero_ld(self, raffle_id: int) -> Dict[str, str]:
        """
        Get the LD number of a raffle
        :param raffle_id: The ID of the raffle
        :return: A dictionary containing the LD number of the raffle
        """
        response = None
        validate_entry = isinstance(raffle_id, int)
        if validate_entry:
            response = self.raffle_repository.get_raffle_numero_ld(raffle_id)
        return {"Success": validate_entry, "Data": response}

    def get_raffle_grupo_fazendinha(self, raffle_id: int) -> Dict[str, str]:
        """
        Get the fazendinha group of a raffle
        :param raffle_id: The ID of the raffle
        :return: A dictionary containing the fazendinha group of the raffle
        """
        response = None
        validate_entry = isinstance(raffle_id, int)
        if validate_entry:
            response = self.raffle_repository.get_raffle_grupo_fazendinha(raffle_id)
        return {"Success": validate_entry, "Data": response}
