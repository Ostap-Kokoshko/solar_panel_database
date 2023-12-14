from my_project.auth.service import solar_system_service
from my_project.auth.controller.general_controller import GeneralController


class SolarSystemController(GeneralController):
    """
    Realisation of SolarSystem controller.
    """
    _service = solar_system_service

    def solar_system_find_solar_panels(self, solar_system_id: int):
        return self._service.solar_system_find_solar_panels(solar_system_id)

    def find_orders(self, solar_system_id: int):
        return self._service.find_orders(solar_system_id)

    def find_owners(self, solar_system_id: int):
        return self._service.find_owners(solar_system_id)

    def insert_into_owner_has_solar_system(self, solar_system_id: int, owner_name: str, owner_email: str,
                                           owner_phone_number: str, owner_city_id: int, owner_region_name: str,
                                           owner_count: int, solar_system_count: int):
        self._service.insert_into_owner_has_solar_system(
            solar_system_id, owner_name, owner_email, owner_phone_number,
            owner_city_id, owner_region_name, owner_count, solar_system_count
        )
