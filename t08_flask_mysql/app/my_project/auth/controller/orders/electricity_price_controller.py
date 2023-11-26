from my_project.auth.service import electricity_price_service
from my_project.auth.controller.general_controller import GeneralController


class ElectricityPriceController(GeneralController):
    """
    Realisation of ElectricityPrice controller.
    """
    _service = electricity_price_service
