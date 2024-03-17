from typing import Dict
from src.models.participate import ParticipateModel as Participate
from src.data.interfaces import PrizeRepositoryInterface


class GenerateAutoMessage:
    """ Class to define use case: Generate Auto Message """
    def __init__(self, prize_repository: Type[PrizeRepositoryInterface]):
        self.prize_repository = prize_repository

    def generate_message(self, auto_message_data: Dict, participate: participate) -> str:
        """Generate message based on auto message data and participant information
        :param auto_message_data: dictionary containing auto message data
        :param participate: participate object
        :return: generated message
        """
        message = auto_message_data['msg']
        # Replace placeholders in the message with participant information
        message = message.replace("<br />", "")
        for key, value in auto_message_data.items():
            if key != 'msg':
                replace = self.replace_key(key, value, participate)
                var = "{" + key + "}"
                message = message.replace(var, replace)
        return message

    def replace_key(self, key: str, value: str, participate: Participate) -> str:
        """Replace a placeholder key with corresponding participant information
        :param key: placeholder key
        :param value: placeholder value
        :param participate: participate object
        :return: replaced value
        """
        if key == 'id':
            return str(participate.id)
        elif key == 'nome':
            return participate.name
        elif key == 'valor':
            return str(participate.rifa().price)
        elif key == 'total':
            return "{:,.2f}".format(participate.valor).replace(",", ".")
        elif key == 'cotas':
            cotas = ','.join(participate.numbers())
            return cotas
        elif key == 'sorteio':
            return participate.rifa().name
        elif key == 'link':
            return f"/pagarReserva/{participate.id}"  # Assuming route function is defined else where
        else:
            return value  # Placeholder value if key not found
