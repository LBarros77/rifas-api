from typing import List
from .participant import ParticipantModel


class ParticipateModel:
    def __init__(
        self,
        id: int,
        numbers: List[str],
        reserveds: List[ParticipantModel],
        payeds: List[ParticipantModel],
        conferred: str
    ) -> None:
        self.id = id
        self.numbers = numbers
        self.reserveds = reserveds
        self.payeds = payeds
        self.conferred = conferred
