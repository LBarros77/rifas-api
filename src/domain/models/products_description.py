import uuid


class ProductsDescriptioEntity:
    def __init__(self,
        id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4())
        description: str,
        video: str
    ) -> None:
        self.id = id
        self.description = description
        self.video = video
