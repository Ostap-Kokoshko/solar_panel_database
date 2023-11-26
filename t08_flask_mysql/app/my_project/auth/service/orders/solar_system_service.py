from my_project.auth.dao import solar_system_dao
from my_project.auth.service.general_service import GeneralService


class SolarSystemService(GeneralService):
    """
    Realisation of SolarSystem service.
    """
    _dao = solar_system_dao

    def solar_system_find_solar_panels(self, solar_system_id: int):
        return self._dao.solar_system_find_solar_panels(solar_system_id)

    def find_orders(self, solar_system_id: int):
        return self._dao.find_orders(solar_system_id)

    def find_owners(self, solar_system_id: int):
        return self._dao.find_owners(solar_system_id)
