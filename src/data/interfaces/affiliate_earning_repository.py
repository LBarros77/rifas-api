from abc import ABC, abstractmethod
from src.domain.models import AffiliateEarningModel as AffiliateEarning


class AffiliateEarningRepositoryInterface(ABC):
    """ Affiliate Earning Repository Interface """
    @abstractmethod
    def select_earnings(self, affiliate_earning_id: str) -> Dict[bool, List[AffiliateEarning]]:
        """Select Earnings By affiliate_earning_id
        :param - affiliate_earning_id: id of the AffiliateEarning
        :return - Dictionary with information about the process
        """
        Exception("Should be needed implament select_affiliate_earners")

    @abstractmethod
    def status(self) -> str: pass
