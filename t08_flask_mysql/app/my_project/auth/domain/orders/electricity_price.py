
from __future__ import annotations

from datetime import datetime
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class ElectricityPrice(db.Model, IDto):
    """
    Model declaration for ElectricityPrice.
    """
    __tablename__ = "electricity_price"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time_date = db.Column(db.DateTime, nullable=False, unique=True)
    price = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"ElectricityPrice(id={self.id}, time_date={self.time_date}, price='{self.price}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "time_date": str(self.time_date),
            "price": self.price,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ElectricityPrice:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ElectricityPrice(
            time_date=datetime.strptime(dto_dict.get("time_date"), "%Y-%m-%d %H:%M:%S"),
            price=dto_dict.get("price"),
        )
        return obj
