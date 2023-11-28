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

    def find_all_panels_and_systems(self):
        all_panels = self._service.find_all()
        all_systems = self._service.find_all_solar_systems()

        combined_data = {
            'solar_panels': [panel.put_into_dto() for panel in all_panels],
            'solar_systems': [system.put_into_dto() for system in all_systems],
        }

        return combined_data

    def find_all_panels_with_batteries(self):
        all_panels = self._service.find_all()
        all_batteries = self._service.find_all_batteries()

        combined_data = {
            'solar_panels': [panel.put_into_dto() for panel in all_panels],
            'batteries': [battery.put_into_dto() for battery in all_batteries],
        }

        return combined_data

    def add_battery_to_solar_panel(self, solar_panel_id: int, battery_id: int):
        self._service.add_battery_to_solar_panel(solar_panel_id, battery_id)

    def remove_battery_from_solar_panel(self, solar_panel_id: int, battery_id: int):
        self._service.remove_battery_from_solar_panel(solar_panel_id, battery_id)

    def find_by_id_with_batteries(self, solar_panel_id: int):
        return self._service.find_by_id_with_batteries(solar_panel_id)
