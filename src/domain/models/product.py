class Product:
    def __init__(
        self,
        id: int,
        name: str,
        slug: str,
        price: float,
        status: str,
        type_raffles: str,
        winner: str,
        draw_prediction: str,
        draw_date: str,
        visible: str,
        favorite: str,
        minimum: str,
        maximum: str,
        expiration: str,
        ranking_quantity: int,
        partial: str,
        gateway: str,
        subname: str,
        zeros_quantity: str,
        game_mode: str,
        numbers: str,
        affiliate_earning: str,
        description: str
    ) -> None:
        self.id = id
        self.name = name
        self.slug = slug
        self.price = price
        self.status = status
        self.type_raffles = type_raffles
        self.winner = winner
        self.draw_prediction = draw_prediction
        self.draw_date = draw_date
        self.visible = visible
        self.favorite = favorite
        self.minimum = minimum
        self.maximum = maximum
        self.expiration = expiration
        self.ranking_quantity = ranking_quantity
        self.partial = partial
        self.gateway = gateway
        self.subname = subname
        self.zeros_quantity = zeros_quantity
        self.game_mode = game_mode
        self.numbers = numbers
        self.affiliate_earning = affiliate_earning
        self.description = description
