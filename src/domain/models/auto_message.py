class AutoMessageEntity:
    def __init__(self,
        id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4())
        description: str,
        destinatary: str,
        msg: str
    ) -> None:
        self.id = id
        self.description = description
        self.destinatary = destinatary
        self.msg = msg
