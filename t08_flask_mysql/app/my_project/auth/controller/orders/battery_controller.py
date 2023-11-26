from my_project.auth.service import battery_service
from my_project.auth.controller.general_controller import GeneralController


class BatteryController(GeneralController):
    """
    Realisation of Battery controller.
    """
    _service = battery_service

    def find_solar_panels(self, battery_id: int):
        return self._service.find_solar_panels(battery_id)
