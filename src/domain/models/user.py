class User:
    def __init__(
        self,
        id: str,
        name: str,
        phone_number: str,
        status: boolean,
        email: str,
        password: str,
        cpf: str,
        pix: str,
        affiliate: boolean,
        remember_token: str,
        timestamps: DateTime
    ) -> None:
        self.id: id
        self.name = name
        self.phone_number = phone_number
        self.status = status
        self.email = email
        self.password = password
        self.cpf = cpf
        self.pix = pix
        self.affiliate = affiliate
        self.remember_token = remember_token
        self.timestamps = timestampss
