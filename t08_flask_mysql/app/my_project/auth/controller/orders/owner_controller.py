from my_project.auth.service import owner_service
from my_project.auth.controller.general_controller import GeneralController


class OwnerController(GeneralController):
    """
    Realisation of Owner controller.
    """
    _service = owner_service

    def owner_find_solar_systems(self, owner_id: int):
        return self._service.owner_find_solar_systems(owner_id)
