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
