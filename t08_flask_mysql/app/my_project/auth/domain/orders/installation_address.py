from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class InstallationAddress(db.Model, IDto):
    """
    Model declaration for InstallationAddress.
    """
    __tablename__ = "installation_address"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(45), nullable=False)
    postal_index = db.Column(db.Integer, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    city_region_name = db.Column(db.String(50), db.ForeignKey('region.name'), nullable=False)

    # Relationship M:1 with City
    city = db.relationship("City", backref="installation_addresses")

    def __repr__(self) -> str:
        return f"InstallationAddress({self.id}, '{self.street}', {self.postal_index}, '{self.city.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "street": self.street,
            "postal_index": self.postal_index,
            "city_id": self.city_id,
            "city_region_name": self.city_region_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> InstallationAddress:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = InstallationAddress(
            street=dto_dict.get("street"),
            postal_index=dto_dict.get("postal_index"),
            city_id=dto_dict.get("city_id"),
            city_region_name=dto_dict.get("city_region_name"),
        )
        return obj