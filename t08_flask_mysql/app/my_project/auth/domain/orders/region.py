from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Region(db.Model, IDto):
    """
    Model declaration for Region.
    """
    __tablename__ = "region"

    name = db.Column(db.String(50), primary_key=True)

    def __repr__(self) -> str:
        return f"Region({self.name})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Region:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Region(
            name=dto_dict.get("name"),
        )
        return obj
