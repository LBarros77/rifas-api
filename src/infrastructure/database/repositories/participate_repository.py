from typing import List
from sqlalchemy import select
from src.data.interfaces.participant_repository import IParticipantRepository
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.domain.models import ParticipateModel, ProductModel, ParticipantModel
from src.infrastructure.database.entities import (
    Participate, Product, PaymentPix
)


class ParticipateRepository(IParticipanteRepository):

    @classmethod
    def get_reserveds(cls) -> List[ParticipantModel]:
        with DBConnectionHandler() as database:
            try:
                products = cls.get_product_game_mode()
                participate_reserveds = database.session.select(Participate)
                    .where(Participate.product_id in products, Participate.reserved == True)
                    .all()
                return participate_reserveds
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def get_reserveds_quantity(cls) -> int:
        return sum(cls.get_reserveds)

    @classmethod
    def status(cls) -> str:
        reserveds_quantity = cls.get_reserveds_quantity()
        payeds_quantity = cls.get_payeds_quantity()
        if reserveds_quantity > 0:
            return "Números Reservados"
        elif payeds_quantity > 0:
            return "Compra Aprovada"
        else:
            return ""
    
    @classmethod
    def get_situation(cls, participate_id: int) -> Dic[str, str]:
        """ Method to get situation desciption """
        with DBConnectionHandler() as database:
            try:
                participate = database.settion.get(Participate, participate_id)
                situation = participate.situation
                return situation
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def get_numbers(cls) -> List:
        with DBConnectionHandler() as database:
            try:
                participant = database.session
                    .query(Participate)
                    .filter_by(len(numbers) > 0)
                    .one_or_none()
                if participant:
                    numbers = participant.numbers.split(", ")
                    return sorted(map(int, numbers))
                return []
            except Exception as exception:
                database.session.rollback()
                return exception

    @classmethod
    def get_numbers_summary(cls) -> List[str]:
        numbers = cls.get_numbers()
        return [str(number) for number in numbers]

    @classmethod
    def get_payeds(cls) -> List[ParticipantModel]:
        with DBConnectionHandler() as database:
            try:
                payed_participants = database.sesstion
                    .query(Participate)
                    .join(Raffle, Raffle.participant_id == Participate.id)
                    .filter(Raffle.status == "Pago", Participate.numbers > 0)
                    .all()
                return payed_participants
            except Exception as exception:
                database.sesstion.rollback()
                return exception

    @classmethod
    def get_payeds_quantity(cls) -> int:
        with DBConnectionHandler() as database:
            try:
                payed_raffles = database.session
                    .query(RaffleModel)
                    .join(Participate, RaffleModel.participant_id == Participate.id, RaffleModel.product_id == ProductModel.id)
                    .filter(Raffle.status == "Pago", Product.game_mode == "numeros")
                    .all()
                return len(payed_raffles)
            except Exception as exception:
                database.session.rollback()
                return exception

    @classmethod
    def get_product_game_mode(cls) -> List[ProductModel]:
        with DBConnectionHandler() as database:
            try:
                products = database.session.select(ProductModel)
                    .where(ProductModel.game_mode == "numeros")
                    .all()
                return products
            except Exception as exception:
                database.session.rollback()
                raise exception
