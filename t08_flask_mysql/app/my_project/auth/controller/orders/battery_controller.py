from my_project.auth.service import battery_service
from my_project.auth.controller.general_controller import GeneralController


class BatteryController(GeneralController):
    """
    Realisation of Battery controller.
    """
    _service = battery_service

    def find_solar_panels(self, battery_id: int):
        return self._service.find_solar_panels(battery_id)

    def add_solar_panel_to_battery(self, battery_id: int, solar_panel_id: int):
        self._service.add_solar_panel_to_battery(battery_id, solar_panel_id)

    def remove_solar_panel_from_battery(self, battery_id: int, solar_panel_id: int):
        self._service.remove_solar_panel_from_battery(battery_id, solar_panel_id)
