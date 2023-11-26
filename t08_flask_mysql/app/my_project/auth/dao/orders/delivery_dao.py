from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Delivery


class DeliveryDAO(GeneralDAO):
    """
    Realisation of Delivery data access layer.
    """
    _domain_type = Delivery
