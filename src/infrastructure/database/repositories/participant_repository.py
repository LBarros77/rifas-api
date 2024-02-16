from typing import List, Integer, String, Boolean
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.infrastructure.database.entities.participant import Participant as ParticipantEntity
from src.data.interfaces.participant_repository import IParticipantRepository
from src.domain.models.participant import Participant as ParticipantModel


class ParticipantRepository(IParticipantRepository):

    @classmethod
    def get_reserveds_by_game_mode(cls, game_mode) -> List[Integer]:
        with DBConnectionHandler as database:
            try:
                reserveds = database.session
                    .query(ParticipantEntity.reserveds)
                    .filter(ParticipantEntity.game_mode == game_mode)
                    .all()
                return reserveds
            except Exception as exception:
                database.session.rollback()
                raise exception
