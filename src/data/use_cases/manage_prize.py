from typing import Dict, Type
from src.data.interfaces import (
    PrizeRepositoryInterface,
    ProductRepositoryInterface,
    ParticipateRepositoryInterface
)


class ManagePrize:
    """ Class to define use case: Manage Prize """
    def __init__(
        self,
        prize_repository: Type[PrizeRepositoryInterface],
        product_repository: Type[ProductRepositoryInterface],
        participate_repository: Type[ParticipateRepositoryInterface]
    ):
        self.prize_repository = prize_repository
        self.product_repository = product_repository
        self.participate_repository = participate_repository

    def get_prize_info(self, prize_id: int) -> Dict:
        """Get prize information by prize ID
        :param prize_id: ID of the prize
        :return: dictionary containing prize information
        """
        prize_info = {}
        prize = prize_repository.find_by_id(prize_id)
        if prize:
            prize_info['product'] = self.get_product_info(prize.product_id)
            prize_info['participant'] = self.get_participant_info(prize.participant_id)
            prize_info['ordem'] = prize.order
            prize_info['phone_number'] = prize.phone_number
            prize_info['description'] = prize.description
            prize_info['earner'] = prize.earner
            prize_info['quota'] = prize.quota
            prize_info['photo'] = prize.photo
            prize_info['link_wpp'] = prize.linkWpp()
        return prize_info

    def get_product_info(self, product_id: int) -> Dict:
        """Get product information by product ID
        :param product_id: ID of the product
        :return: dictionary containing product information
        """
        product_info = {}
        # Assuming ProductRepository is available and has methods to fetch product information
        product = self.product_repository.find_by_id(product_id)
        if product:
            product_info['name'] = product.name
            product_info['slug'] = product.slug
            product_info['price'] = product.price
            # Add more product information as needed
        return product_info

    def get_participant_info(self, participant_id: int) -> Dict:
        """Get participant information by participant ID
        :param participant_id: ID of the participant
        :return: dictionary containing participant information
        """
        participant_info = {}
        if participant_id:
            participant = self.participate_repository.find_by_id(participant_id)
            if participant:
                participant_info['name'] = participant.name
                participant_info['email'] = participant.email
                participant_info['phone'] = participant.phone
                # Add more participant information as needed
        return participant_info
