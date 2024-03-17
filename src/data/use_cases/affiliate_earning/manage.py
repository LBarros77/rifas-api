from typing import Dict, List, Type
from src.data.interfaces import AffliliateEarningRepositoryInterface as AffliliateEarningRepository


class ManageAffiliateEarning:
    """ Class to define use case: Manage GanhosAfiliado """
    def __init__(self, ganhos_afiliado_repository: Type[AffliliateEarningRepository]):
        self.ganhos_afiliado_repository = ganhos_afiliado_repository

    def update_ganhos_afiliado_status(self, ganhos_afiliado_id: int, novo_status: str) -> Dict[bool, str]:
        """Update status of GanhosAfiliado
        :param - ganhos_afiliado_id: id of the GanhosAfiliado
        :param - novo_status: new status to be set
        :return - Dictionary with information about the process
        """
        response = None
        validate_entry = isinstance(ganhos_afiliado_id, int) and isinstance(novo_status, str)
        if validate_entry:
            response = self.ganhos_afiliado_repository.update_ganhos_afiliado_status(ganhos_afiliado_id, novo_status)
        return {"Success": validate_entry, "Message": response}
