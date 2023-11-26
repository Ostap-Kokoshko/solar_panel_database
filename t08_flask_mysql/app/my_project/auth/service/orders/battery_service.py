from my_project.auth.dao import battery_dao
from my_project.auth.service.general_service import GeneralService


class BatteryService(GeneralService):
    """
    Realisation of Battery service.
    """
    _dao = battery_dao

    def find_solar_panels(self, battery_id: int):
        return self._dao.find_solar_panels(battery_id)
