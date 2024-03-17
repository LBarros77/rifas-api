from typing import List
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.data.interfaces.raffle_repository import IRaffleRepository
from src.infrastructure.database.entities.raffle import Raffle, Participant
from src.domain.models import ProductModel, ParticipantModel


class RaffleRepository(IRaffleRepository):

    @classmethod
    def get_raffle(cls, product_id: int) -> ProductModel:
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
    def get_participant(cls, participant_id: str) -> ParticipantModel:
        with DBConnectionHandler as database:
            try:
                participant = database.session
                    .query(ParticipantModel)
                    .find_by(participant_id == participant_id)
                return participant
            except Exeception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def get_number(cls):
        with DBConnectionHandler() as database:
            try:
                raffle = database.session.query(Raffle).filter(Raffle.number).first()
                return raffle.number
            except Exception as exception:
                database.session.rollback()
                raise exception
