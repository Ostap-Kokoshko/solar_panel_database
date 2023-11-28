
from __future__ import annotations

from datetime import datetime
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy import UniqueConstraint, Index


class EnergySale(db.Model, IDto):
    """
    Model declaration for EnergySale.
    """
    __tablename__ = "energy_sale"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Integer, nullable=True)
    electricity_price_id = db.Column(db.Integer, db.ForeignKey('electricity_price.id'), nullable=False)

    # Relationship M:1 with ElectricityPrice
    electricity_prices = db.relationship("ElectricityPrice", back_populates="energy_sales")

    __table_args__ = (
        UniqueConstraint('id', 'electricity_price_id'),
        Index('fk_energy_sale_electricity_price1_idx', 'electricity_price_id'),
        {},
    )

    def __repr__(self) -> str:
        return f"EnergySale(id={self.id}, quantity={self.quantity}, electricity_price_id={self.electricity_price_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "quantity": self.quantity,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EnergySale:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = EnergySale(
            quantity=dto_dict.get("quantity"),
            electricity_price_id=dto_dict.get("electricity_price_id"),
        )
        return obj
