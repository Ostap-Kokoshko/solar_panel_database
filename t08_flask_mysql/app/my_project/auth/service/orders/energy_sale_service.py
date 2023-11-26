from my_project.auth.dao import energy_sale_dao
from my_project.auth.service.general_service import GeneralService


class EnergySaleService(GeneralService):
    """
    Realisation of EnergySale service.
    """
    _dao = energy_sale_dao
