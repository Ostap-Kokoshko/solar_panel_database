from my_project.auth.dao import region_dao
from my_project.auth.service.general_service import GeneralService


class RegionService(GeneralService):
    """
    Realisation of Region service.
    """
    _dao = region_dao
