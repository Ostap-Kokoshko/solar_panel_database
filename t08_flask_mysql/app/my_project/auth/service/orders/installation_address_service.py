from my_project.auth.dao import installation_address_dao
from my_project.auth.service.general_service import GeneralService


class InstallationAddressService(GeneralService):
    """
    Realisation of InstallationAddress service.
    """
    _dao = installation_address_dao
