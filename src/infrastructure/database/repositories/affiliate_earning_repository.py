from src.data.interface.affiliate_earning import IAffiliateEarningRepository


class AffiliateEarningRepository(IAffiliateEarningRepository):

    @classmethod
    def status(cls) -> str:
        solicitation = cls.solicitation()
        if solicitation is not None:
            return "RECEBIDO" if solicitation.payed else "SOLICITADO"
        return "DISPONÍVEL"
