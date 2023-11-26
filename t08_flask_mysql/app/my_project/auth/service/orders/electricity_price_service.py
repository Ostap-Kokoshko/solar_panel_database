from my_project.auth.dao import electricity_price_dao
from my_project.auth.service.general_service import GeneralService


class ElectricityPriceService(GeneralService):
    """
    Realisation of ElectricityPrice service.
    """
    _dao = electricity_price_dao
