class OrderEntity:
    def __init__(self, key_pix: str, participant_id: int, dadas: str, price: float) -> None:
        self.key_pix = key_pix
        self.participant_id = participant_id
        self.dadas = dadas
        self.price = price
