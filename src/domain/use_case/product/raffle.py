from abc import ABC, abstractmethod
from typing import List


class RaffleUseCaseInterface(ABC):
    """ Raffle Use Case Interface to implement methods"""

    def get_raffle_status(self, raffle_id: int) -> Dict[str, str]:
        """
        Get the status of a raffle
        :param raffle_id: The ID of the raffle
        :return: A dictionary containing the status of the raffle
        """
        raise Exception("Should implement method: get_raffle_status")

    def get_raffle_group(self, raffle_id: int) -> Dict[str, str]:
        """
        Get the group of a raffle
        :param raffle_id: The ID of the raffle
        :return: A dictionary containing the group of the raffle
        """
        raise Exception("Should implement method: numget_raffle_groupbers")

    def get_raffle_group_side(self, raffle_id: int) -> Dict[str, str]:
        """
        Get the group side of a raffle
        :param raffle_id: The ID of the raffle
        :return: A dictionary containing the group side of the raffle
        """
        raise Exception("Should implement method: get_raffle_group_side")

    def get_raffle_numero_ld(self, raffle_id: int) -> Dict[str, str]:
        """
        Get the LD number of a raffle
        :param raffle_id: The ID of the raffle
        :return: A dictionary containing the LD number of the raffle
        """
        raise Exception("Should implement method: get_raffle_numero_ld")

    def get_raffle_grupo_fazendinha(self, raffle_id: int) -> Dict[str, str]:
        """
        Get the fazendinha group of a raffle
        :param raffle_id: The ID of the raffle
        :return: A dictionary containing the fazendinha group of the raffle
        """
        raise Exception("Should implement method: get_raffle_grupo_fazendinha")
