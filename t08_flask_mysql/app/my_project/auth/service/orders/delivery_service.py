from my_project.auth.dao import delivery_dao
from my_project.auth.service.general_service import GeneralService


class DeliveryService(GeneralService):
    """
    Realisation of Delivery service.
    """
    _dao = delivery_dao
