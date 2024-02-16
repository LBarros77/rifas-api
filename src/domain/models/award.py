class Award:
    def __init__(
        self,
        product_id: int,
        participant_id: int,
        order: str,
        phone_number: int,
        description: str,
        winner: str,
        quota: str,
        photo: str
    ) -> None:
        self.product_id product_id
        self.participant_id = participant_id
        self.order = order
        self.phone_number = phone_number
        self.description = description
        self.winner = winner
        self.quota = quota
        self.photo = photo
