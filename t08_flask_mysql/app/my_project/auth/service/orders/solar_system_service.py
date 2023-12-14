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

    def insert_into_owner_has_solar_system(self, solar_system_id: int, owner_name: str, owner_email: str,
                                           owner_phone_number: str, owner_city_id: int, owner_region_name: str,
                                           owner_count: int, solar_system_count: int):
        self._dao.insert_into_owner_has_solar_system(
            solar_system_id, owner_name, owner_email, owner_phone_number,
            owner_city_id, owner_region_name, owner_count, solar_system_count
        )
