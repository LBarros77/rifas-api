import uuid


class RaffleEntity:
    def __init__(
        self,
        id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4()),
        number: int,
        product_id: int,
        participant_id: str,
        status: str
    ) -> None:
        self.id = id
        self.number = number
        self.product_id = product_id
        self.participant_id = participant_id
        self.status = status
