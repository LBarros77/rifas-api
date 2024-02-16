from abc import ABC, abstractmethod
from typing import List
from src.domain.models.participant import Participant


class IParticipantRepository(ABC):

    @abstractmethod
    def get_reserveds(self) -> List: pass

    @abstractmethod
    def reserveds_quantity(self) -> int: pass

    @abstractmethod
    def get_numbers(self) -> int: pass

    @abstractmethod
    def status(self) -> bool: pass

    @abstractmethod
    def status_badge(self) -> bool: pass

    @abstractmethod
    def situation(self) -> str: pass

    @abstractmethod
    def payeds_quantity(self) -> int: pass
