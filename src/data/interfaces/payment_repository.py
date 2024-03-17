from abc import ABC, abstractmethod


class PaymentRepositoryInterface(ABC):
    ''' Interface for payment methods '''

    @abstractmethod
    def confirm_payment(self, participant_id) -> bool: pass
