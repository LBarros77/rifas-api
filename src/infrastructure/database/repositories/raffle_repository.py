from typing import List
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.data.interfaces.raffle_repository import IRaffleRepository
from src.infrastructure.database.entities.raffle import (
    Raffle as RaffleEntity,
    Participant as ParticipantEntity
)
from src.domain.models import Product, Participant


class RaffleRepository(IRaffleRepository):

    @classmethod
    def get_raffle(cls, product_id: int) -> Product:
        with DBConnectionHandler as database:
            try:
                raffle = database.session
                    .query(RaffleEntity)
                    .find_by(product_id == product_id)
                return raffle
            except Exceptio as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def get_participant(cls, participant_id) -> Participant:
        with DBConnectionHandler as database:
            try:
                participant = database.session
                    .query(ParticipantEntity)
                    .find_by(participant_id == participant_id)
                return participant
            except Exeception as exception:
                database.session.rollback()
                raise exception
