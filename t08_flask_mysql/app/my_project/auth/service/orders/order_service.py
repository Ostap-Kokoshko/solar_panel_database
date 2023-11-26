from my_project.auth.dao import order_dao
from my_project.auth.service.general_service import GeneralService


class OrderService(GeneralService):
    """
    Realisation of Order service.
    """
    _dao = order_dao

    def find_solar_systems(self, order_id: int):
        return self._dao.find_solar_systems(order_id)
