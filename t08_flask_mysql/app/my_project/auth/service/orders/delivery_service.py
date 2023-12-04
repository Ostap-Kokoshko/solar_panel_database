from my_project.auth.dao import delivery_dao
from my_project.auth.service.general_service import GeneralService


class DeliveryService(GeneralService):
    """
    Realisation of Delivery service.
    """
    _dao = delivery_dao

    def add_delivery(self, name: str, price: int):
        self._dao.insert_into_delivery(name, price)

    def insert_ten_deliveries(self):
        self._dao.insert_ten_into_delivery()

    def get_delivery_stats(self, stat_type: str) -> int:
        return self._dao.get_delivery_stats(stat_type)

    def dynamic_table_creation(self):
        self._dao.dynamic_table_creation()