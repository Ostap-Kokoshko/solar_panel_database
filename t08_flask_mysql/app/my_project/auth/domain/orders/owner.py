from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

owner_solar_system = db.Table(
    'owner_solar_system',
    db.Column('owner_id', db.Integer, db.ForeignKey('owner.id'), primary_key=True),
    db.Column('solar_system_id', db.Integer, db.ForeignKey('solar_system.id'), primary_key=True),
    db.UniqueConstraint('owner_id', 'solar_system_id', name='uq_owner_solar_system'),
    extend_existing=True
)


class Owner(db.Model, IDto):
    """
    Model declaration for Owner.
    """
    __tablename__ = "owner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)
    phone_number = db.Column(db.String(13), unique=True, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    city_region_name = db.Column(db.String(50), db.ForeignKey('city_region.name'), nullable=False)

    # Relationship M:1 with City
    city = db.relationship("City", backref="owners")
    solar_systems = db.relationship("SolarSystem", secondary="owner_solar_system",
                                    back_populates="owners")


    def __repr__(self) -> str:
        return f"Owner({self.id}, '{self.name}', '{self.email}', '{self.phone_number}', '{self.city.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "city_id": self.city_id,
            "city_region_name": self.city_region_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Owner:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Owner(
            name=dto_dict.get("name"),
            email=dto_dict.get("email"),
            phone_number=dto_dict.get("phone_number"),
            city_id=dto_dict.get("city_id"),
            city_region_name=dto_dict.get("city_region_name"),
        )
        return obj
