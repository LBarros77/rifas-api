class ProductBkpEntity:
    def __init__(
        self,
        name: str,
        slug: str,
        price: float,
        status: boolean,
        type_raffles: str,
        winner: str,
        draw_prediction: str,
        draw_date: str,
        visible: boolean,
        favoritie: boolean,
        minimum: int,
        maximum: int,
        expiration: str,
        ranking_quantity: int,
        parcial: str,
        gateway: str,
        subname: str,
        zeros_quantity: int,
        game_mode: str
    ) -> None:
        self.name = name
        self.slug = slug
        self.price = price
        self.status = status
        self.type_raffles = type_raffles
        self.winner = winner
        self.draw_prediction = draw_prediction
        self.draw_date = draw_date
        self.visible = visible
        self.favoritie = favoritie
        self.minimum = minimum
        self.maximum = maximum
        self.expiration = expiration
        self.qtd_ranking = qtd_ranking
        self.parcial = parcial
        self.gateway = gateway
        self.subname = subname
        self.qtd_zeros = qtd_zeros
        self.game_mode = game_mode
