from typing import Dict, List, Type
from src.domain.models import AffiliateEarningModel as AffiliateEarning
from src.data.interfaces import AffiliateEarningRepositoryInterface as AffiliateEarningRepository


class FindAffiliateEarnig:
    """ Class to define use case: Find GanhosAfiliado """
    def __init__(self, affiliate_earning_repository: Type[AffiliateEarningRepository]):
        self.affiliate_earning_repository = affiliate_earning_repository

    def by_affiliate_earning_id(self, affiliate_earning_id: int) -> Dict[bool, List[AffiliateEarning]]:
        """Select Earnings By affiliate_earning_id
        :param - affiliate_earning_id: id of the GanhosAfiliado
        :return - Dictionary with information about the process
        """
        response = None
        validate_entry = isinstance(affiliate_earning_id, int)
        if validate_entry:
            response = self.affiliate_earning_repository.select_earnings(affiliate_earning_id=affiliate_earning_id)
        return {"Success": validate_entry, "Data": response}
