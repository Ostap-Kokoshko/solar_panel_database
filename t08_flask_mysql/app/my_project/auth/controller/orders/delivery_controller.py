from my_project.auth.service import delivery_service
from my_project.auth.controller.general_controller import GeneralController


class DeliveryController(GeneralController):
    """
    Realisation of Delivery controller.
    """
    _service = delivery_service

    def add_delivery(self, name: str, price: int):
        self._service.add_delivery(name, price)

    def insert_ten_deliveries(self):
        self._service.insert_ten_deliveries()

    def get_delivery_stats(self, stat_type: str):
        return self._service.get_delivery_stats(stat_type)
