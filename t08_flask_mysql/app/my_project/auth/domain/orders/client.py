
from __future__ import annotations

from datetime import datetime
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy import UniqueConstraint, Index


class Client(db.Model, IDto):
    """
    Model declaration for Client.
    """
    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.DECIMAL, unique=True, nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    email = db.Column(db.String(45), nullable=True)
    gander = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    city_region_name = db.Column(db.String(50), db.ForeignKey('region.name'), nullable=False)

    # Relationship M:1 with City
    city = db.relationship("City", backref="clients_association")

    __table_args__ = (
        UniqueConstraint('phone'),
        Index('fk_client_city1_idx', 'city_id', 'city_region_name'),
        {},
    )

    def __repr__(self) -> str:
        return f"Client(id={self.id}, name='{self.name}', lastname='{self.lastname}', phone={self.phone}, gander='{self.gander}', city_id={self.city_id}, city_region_name='{self.city_region_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "phone": str(self.phone),
            "birthday": str(self.birthday) if self.birthday else None,
            "email": self.email,
            "gander": self.gander,
            "age": self.age,
            "city_id": self.city_id,
            "city_region_name": self.city_region_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Client:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Client(
            name=dto_dict.get("name"),
            lastname=dto_dict.get("lastname"),
            phone=dto_dict.get("phone"),
            birthday=datetime.strptime(dto_dict.get("birthday"), "%Y-%m-%d") if dto_dict.get("birthday") else None,
            email=dto_dict.get("email"),
            gander=dto_dict.get("gander"),
            age=dto_dict.get("age"),
            city_id=dto_dict.get("city_id"),
            city_region_name=dto_dict.get("city_region_name"),
        )
        return obj
