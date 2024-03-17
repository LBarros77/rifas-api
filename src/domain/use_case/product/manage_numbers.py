from abc import ABC, abstractmethod
from typing import List


class ManageNumbers(ABC):
    """ Manage Number from Product """

    @abstractmethod
    def save_numbers(self, numbers_array: List[str]) -> str:
        ''' Join numbers of array and update this numbers '''
        raise Exception("Should implement method: save_numbers")

    @abstractmethod
    def numbers(self) -> List[str]:
        ''' Identify if game mode is numbers and return one list of this numbers
        else return id from product relationed to raffle
        '''
        raise Exception("Should implement method: numbers")
