class CustomerEntity:
    def __init__(self,
        id: str,
        name: str,
        phone_number: str,
        email: str,
        cpf: str
    ) -> None:
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.cpf = cpf
