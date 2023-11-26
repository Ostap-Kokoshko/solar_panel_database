from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy import UniqueConstraint

solar_panel_has_battery = db.Table(
    'solar_panel_has_battery',
    db.Column('solar_panel_id', db.Integer, db.ForeignKey('solar_panel.id')),
    db.Column('battery_id', db.Integer, db.ForeignKey('battery.id')),
    db.UniqueConstraint('solar_panel_id', 'battery_id', name='uq_solar_panel_has_battery'),
    extend_existing=True
)


class Battery(db.Model, IDto):
    """
    Model declaration for Battery.
    """
    __tablename__ = "battery"

    capacity = db.Column(db.Integer, nullable=False)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)

    # Relationship M:M with SolarPanel
    solar_panels = db.relationship("SolarPanel", secondary="solar_panel_has_battery", back_populates="batteries")

    __table_args__ = (
        UniqueConstraint('name'),
        {},
    )

    def __repr__(self) -> str:
        return f"Battery(capacity={self.capacity}, id={self.id}, name='{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "capacity": self.capacity,
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Battery:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Battery(
            capacity=dto_dict.get("capacity"),
            name=dto_dict.get("name"),
        )
        return obj
