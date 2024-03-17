from abc import ABC, abstractmethod
from typing import List, Integer, String, Boolean
from src.domain.models import Product, Participant


class RaffleRepositoryInterface(ABC):

    @abstractmethod
    def get_raffle(self) -> Product: pass

    @abstractmethod
    def get_participant(self) -> Participant: pass

    @abstractmethod
    def get_number(self) -> String: pass
