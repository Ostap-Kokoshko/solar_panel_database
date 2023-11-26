from my_project.auth.service import delivery_service
from my_project.auth.controller.general_controller import GeneralController


class DeliveryController(GeneralController):
    """
    Realisation of Delivery controller.
    """
    _service = delivery_service
