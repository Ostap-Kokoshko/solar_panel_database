from my_project.auth.dao import battery_dao
from my_project.auth.service.general_service import GeneralService


class BatteryService(GeneralService):
    """
    Realisation of Battery service.
    """
    _dao = battery_dao

    def find_solar_panels(self, battery_id: int):
        return self._dao.find_solar_panels(battery_id)

    def add_solar_panel_to_battery(self, battery_id: int, solar_panel_id: int):
        self._dao.add_solar_panel_to_battery(battery_id, solar_panel_id)

    def remove_solar_panel_from_battery(self, battery_id: int, solar_panel_id: int):
        self._dao.remove_solar_panel_from_battery(battery_id, solar_panel_id)
