from my_project.auth.dao import solar_panel_dao
from my_project.auth.service.general_service import GeneralService


class SolarPanelService(GeneralService):
    """
    Realisation of SolarPanel service.
    """
    _dao = solar_panel_dao

    def find_battery(self, solar_panel_id: int):
        return self._dao.find_battery(solar_panel_id)

    def solar_panel_find_solar_systems(self, solar_panel_id: int):
        return self._dao.solar_panel_find_solar_systems(solar_panel_id)

    def find_all_batteries(self):
        return self._dao.find_all_batteries()

    def find_all_solar_systems(self):
        return self._dao.find_all_solar_systems()

    def find_all_panels_and_systems(self):
        all_panels = self._dao.find_all()
        all_systems = self._dao.find_all_solar_systems()

        combined_data = {
            'solar_panels': [panel.put_into_dto() for panel in all_panels],
            'solar_systems': [system.put_into_dto() for system in all_systems],
        }

        return combined_data

    def find_all_panels_with_batteries(self):
        all_panels = self._dao.find_all()
        all_batteries = self._dao.find_all_batteries()

        combined_data = {
            'solar_panels': [panel.put_into_dto() for panel in all_panels],
            'batteries': [battery.put_into_dto() for battery in all_batteries],
        }

        return combined_data

    def add_battery_to_solar_panel(self, solar_panel_id: int, battery_id: int):
        self._dao.add_battery_to_solar_panel(solar_panel_id, battery_id)

    def remove_battery_from_solar_panel(self, solar_panel_id: int, battery_id: int):
        self._dao.remove_battery_from_solar_panel(solar_panel_id, battery_id)

    def find_by_id_with_batteries(self, solar_panel_id: int):
        return self._dao.find_by_id_with_batteries(solar_panel_id)
