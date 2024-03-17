from src.infrastructure.database.settings.connection import DBConnection
from src.domain.models.participant import Participant as ParticipantModel
from src.infrastructure.database.entities.participant import Participant


class PaymentRepository(IPaymentRepository):
    ''' Class Repository implement methods to provide content for payments '''

    @classmethod
    def get_participant(cls, participant_id: str) -> ParticipantModel:
        with DBConnection() as database:
            try:
                participant = database.session
                    .query(Participant)
                    .Filter_by(participant_id == participant_id)
                    .first()
                return participant
            except Exception as exception:
                database.session.rollback()
                return exception

    @classmethod
    def confirm_payment(cls, participante_id) -> bool:
        ''' confirm payment by game mode or participant id
        :param - participante_id is id of the participant_id
        :return - return true if payment is payed
        '''
