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
