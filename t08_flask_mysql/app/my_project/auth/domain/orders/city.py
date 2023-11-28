
from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class City(db.Model, IDto):
    """
    Model declaration for City.
    """
    __tablename__ = "city"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    region_name = db.Column(db.String(50), db.ForeignKey('region.name'), nullable=False)
    regions = db.relationship("Region", back_populates="cities")
    clients = db.relationship("Client", backref="cities", lazy="dynamic")

    def __repr__(self) -> str:
        return f"City({self.id}, '{self.name}', '{self.region.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "region_name": self.region_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> City:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = City(
            name=dto_dict.get("name"),
            region_name=dto_dict.get("region_name"),
        )
        return obj
