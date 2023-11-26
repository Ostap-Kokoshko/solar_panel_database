from my_project.auth.service import order_service
from my_project.auth.controller.general_controller import GeneralController


class OrderController(GeneralController):
    """
    Realisation of Order controller.
    """
    _service = order_service

    def find_solar_systems(self, order_id: int):
        return self._service.find_solar_systems(order_id)
