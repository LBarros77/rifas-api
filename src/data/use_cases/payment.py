from typing import Type
from src.data.interfaces import PaymentRepositoryInterface
from src.domain.user_case import PaymentUseCaseInterface


class Payment(PaymentUseCaseInterface):
    ''' Class implement methods to manage payment forms '''

    def __init__(self, product_repository: Type[PaymentRepositoryInterface]) -> None:
        self.product_repository = product_repository

    def save_numbers(self, product_id: int, numbers_array: List[int]) -> None:
        """ Save numbers for a specific product """

        numbers_str = ",".join([str(num) for num in numbers_array])
        self.product_repository.save_numbers(product_id, numbers_str)

    def get_numbers(self, product_id: int) -> List[int]:
        """ Retrieve numbers for a specific product """

        product = self.product_repository.get_product_by_id(product_id)

        if product.game_mode == 'numeros':
            return [int(num) for num in product.numbers.split(",")]
        else:
            raffle_numbers = self.product_repository.get_raffle_numbers(product_id)
            return raffle_numbers if raffle_numbers else []

    def confirm_payment(self, product_id: int, participant_id: int) -> None:
        """ Confirm payment for a product by a participant """
        product = self.product_repository.get_product_by_id(product_id)
        if product.game_mode == 'numeros':
            participant = self.product_repository.get_participant_by_id(participant_id)
            numbers_participant = self.product_repository.get_participant_numbers(participant_id)
            participant.update({'reservados': 0, 'pagos': len(numbers_participant)})
        else:
            participant = self.product_repository.get_participant_by_id(participant_id)
            numbers_participant = self.product_repository.get_participant_numbers(participant_id)
            participant.update({'reservados': 0, 'pagos': len(numbers_participant)})
            self.product_repository.update_raffle_status(product_id, participant_id)
        self.product_repository.send_whatsapp_message(participant_id)

    def check_afiliate(self, product_id: int, user_id: int) -> bool:
        """ Check if a user is affiliated to a product """
        return self.product_repository.is_user_affiliated(product_id, user_id)

    def get_affiliate_token(self, product_id: int, user_id: int) -> str:
        """ Get affiliate token for a user in a product """
        return self.product_repository.get_affiliate_token(product_id, user_id)
