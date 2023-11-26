from my_project.auth.service import solar_panel_service
from my_project.auth.controller.general_controller import GeneralController


class SolarPanelController(GeneralController):
    """
    Realisation of SolarPanel controller.
    """
    _service = solar_panel_service

    def find_battery(self, solar_panel_id: int):
        return self._service.find_battery(solar_panel_id)

    def solar_panel_find_solar_systems(self, solar_panel_id: int):
        return self._service.solar_panel_find_solar_systems(solar_panel_id)
