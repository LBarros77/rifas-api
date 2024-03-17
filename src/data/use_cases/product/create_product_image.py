class CreateProductImage:
    """" Create Product Image User Case """
    def __init__(self, product_repository: Type[ProductRepositoryInterface]):
        self.product_repository = product_repository

    def create_image(self) -> None:
        """ Create a Product Image """
        # Code to create product image