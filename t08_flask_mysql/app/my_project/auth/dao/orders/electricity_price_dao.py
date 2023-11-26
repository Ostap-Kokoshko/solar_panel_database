from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import ElectricityPrice


class ElectricityPriceDAO(GeneralDAO):
    """
    Realisation of ElectricityPrice data access layer.
    """
    _domain_type = ElectricityPrice
