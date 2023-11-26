from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Client


class ClientDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Client

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Client objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.name == name).order_by(Client.name).all()

    def find_by_number(self, number: int) -> List[object]:
        """
        Gets Client objects from database table by field 'number'.
        :param number: number value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.number == number).order_by(Client.number.desc()).all()
