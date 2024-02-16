class Promotion:
    def __init__(self, qtd_numbers: int, order: int, descont: float, value: float, product_id: int) -> None:
        self.qtd_numbers = qtd_numbers
        self.order = order
        self.descont = descont
        self.value = value
        self.product_id = product_id
