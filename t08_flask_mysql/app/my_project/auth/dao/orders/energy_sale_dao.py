from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import EnergySale


class EnergySaleDAO(GeneralDAO):
    """
    Realisation of EnergySale data access layer.
    """
    _domain_type = EnergySale
