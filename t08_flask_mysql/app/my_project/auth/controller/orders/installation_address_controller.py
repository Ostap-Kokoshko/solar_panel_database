from my_project.auth.service import installation_address_service
from my_project.auth.controller.general_controller import GeneralController


class InstallationAddressController(GeneralController):
    """
    Realisation of InstallationAddress controller.
    """
    _service = installation_address_service
