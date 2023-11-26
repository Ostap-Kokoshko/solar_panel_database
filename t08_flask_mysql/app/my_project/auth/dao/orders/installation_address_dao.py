from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import InstallationAddress


class InstallationAddressDAO(GeneralDAO):
    """
    Realisation of InstallationAddress data access layer.
    """
    _domain_type = InstallationAddress
