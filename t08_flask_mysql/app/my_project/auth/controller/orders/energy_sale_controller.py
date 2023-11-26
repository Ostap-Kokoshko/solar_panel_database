from my_project.auth.service import energy_sale_service
from my_project.auth.controller.general_controller import GeneralController


class EnergySaleController(GeneralController):
    """
    Realisation of EnergySale controller.
    """
    _service = energy_sale_service
