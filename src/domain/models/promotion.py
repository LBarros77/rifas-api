class PromotionEntity:
    def __init__(
        self,
        numbers_quantity: int,
        order: int,
        descont: float,
        value: float,
        product_id: int
    ) -> None:
        self.numbers_quantity = numbers_quantity
        self.order = order
        self.descont = descont
        self.value = value
        self.product_id = product_id
