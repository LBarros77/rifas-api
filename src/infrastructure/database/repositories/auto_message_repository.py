from typing import List
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.data.interfaces.participant_repository import IAutoMessageRepository
from src.domain.models import Participant as ParticipantModel
from src.infrastructure.database.entities import Participant


class AutoMessageRepository(IAutoMessageRepository):

    @classmethod
    def get_message(cls, Participant: ParticipantModel) -> str:
        variables = [
            'id',
            'name',
            'price',
            'total',
            'quotes',
            'prize_draw',
            'link'
        ]
        message = cls.msg.replace("<br />", "")
        for variable in variables:
            replace = self.replace_key(variable, participant)
            var = "{" + variable + "}"
            message = message.replace(var, replace)
        return message

        @classmethod
    def replace_key(cls, key: str, participant: ParticipantModel) -> Union[int, str]:
        if key == 'id':
            return participant.id
        elif key == 'name':
            return participant.name
        elif key == 'price':
            return participant.rifa().price
        elif key == 'total':
            return "{:.2f}".format(participant.valor).replace(".", ",")
        elif key == 'quotes':
            cotas = ",".join(map(str, participant.numbers()))
            return cotas
        elif key == 'prize_draw':
            return participant.rifa().name
        elif key == 'link':
            return f"route('pagarReserva', {participant.id})"
        else:
            return key
