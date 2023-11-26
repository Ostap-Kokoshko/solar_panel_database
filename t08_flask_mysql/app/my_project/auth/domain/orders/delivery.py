
from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Delivery(db.Model, IDto):
    """
    Model declaration for Delivery.
    """
    __tablename__ = "delivery"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=True)
    price = db.Column(db.Integer, nullable=True)

    # Relationship 1:M with Order
    orders = db.relationship("Order", backref="deliveries", lazy="dynamic")

    def __repr__(self) -> str:
        return f"Delivery(id={self.id}, name='{self.name}', price={self.price})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Delivery:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Delivery(
            name=dto_dict.get("name"),
            price=dto_dict.get("price"),
        )
        return obj
