from typing import Type, Dict
from src.data.interfaces import PaymentRepositoryInterface


class ConfirmPayment:
    """ Class to define use case: Confirm Payment """
    def __init__(self, product_repository: Type[PaymentRepositoryInterface]):
        self.product_repository = product_repository

    def confirm_payment(self, product_id: int, participante_id: int) -> Dict[bool, str]:
        """Confirm payment for a product
        :param - product_id: id of the product
        :param - participante_id: id of the participant
        :return - Dictionary with information about the process
        """
        response = None
        validate_entry = isinstance(product_id, int) and isinstance(participante_id, int)
        if validate_entry:
            response = self.product_repository.confirm_payment(product_id, participante_id)
        return {"Success": validate_entry, "Message": response}