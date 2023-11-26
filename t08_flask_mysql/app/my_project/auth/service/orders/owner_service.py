from my_project.auth.dao import owner_dao
from my_project.auth.service.general_service import GeneralService


class OwnerService(GeneralService):
    """
    Realisation of Owner service.
    """
    _dao = owner_dao

    def owner_find_solar_systems(self, owner_id: int):
        return self._dao.owner_find_solar_systems(owner_id)
