class AffiliateEarning:
    def __init__(
        self,
        product_id: int,
        participant_id: int,
        affiliate_id: int,
        value: float,
        payed: float
    ) -> None:
        self.product_id = product_id
        self.participant_id = participant_id
        self.affiliate_id = affiliate_id
        self.value = value
        self.payed = payed
