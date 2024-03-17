import pytest
from typing import List
from src.infrastructure.database.settings.connection import DBConnectionHandler
from src.infrastructure.database.repositories import ParticipantRepository


db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()
participant_repository = ParticipantRepository()

def test_get_reserveds():
    reserved_participants = participant_repository.get_reserveds()
    for participant in reserved_participants:
        if participant.reserved is not True:
            assert participant.reserved == True
    assert reserved_participants.reserved == True

def test_get_numbers():
    numbers = participant_repository.get_numbers()
    assert type(numbers) == List

def test_get_payeds_quantity():
    payeds_quantity = participant_repository.get_payeds_quantity()
    assert payeds_quantity >= 0

def test_get_product_game_mode():
    products = participant_repository.get_product_game_mode()
    assert porducts.game_mode == "numeros"
