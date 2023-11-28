from __future__ import annotations

from datetime import datetime
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy import Index

solar_panel_has_battery = db.Table(
    'solar_panel_has_battery',
    db.Column('solar_panel_id', db.Integer, db.ForeignKey('solar_panel.id')),
    db.Column('battery_id', db.Integer, db.ForeignKey('battery.id')),
    db.UniqueConstraint('solar_panel_id', 'battery_id', name='uq_solar_panel_has_battery'),
    extend_existing=True
)

solar_system_has_solar_panel = db.Table(
    'solar_system_has_solar_panel',
    db.Column('solar_system_id', db.Integer, db.ForeignKey('solar_system.id'), primary_key=True),
    db.Column('solar_panel_id', db.Integer, db.ForeignKey('solar_panel.id'), primary_key=True),
    db.UniqueConstraint('solar_system_id', 'solar_panel_id', name='uq_solar_system_has_solar_panel'),
    extend_existing=True
)


class SolarPanel(db.Model, IDto):
    """
    Model declaration for SolarPanel.
    """
    __tablename__ = "solar_panel"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(45), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    is_tilt_angel = db.Column(db.Boolean, nullable=False)
    tilt_angle = db.Column(db.Integer, nullable=True)
    time = db.Column(db.Time, nullable=False)
    battery_charge = db.Column(db.Integer, nullable=True)
    energy_sale_id = db.Column(db.Integer, db.ForeignKey('energy_sale.id'), nullable=False)
    energy_sale_electricity_price_id = db.Column(db.Integer, db.ForeignKey('electricity_price.id'),
                                                 nullable=False)

    # Relationship M:1 with EnergySale
    energy_sale = db.relationship("EnergySale", backref="solar_panels")
    # Relationship M:M with Battery
    batteries = db.relationship("Battery", secondary="solar_panel_has_battery", back_populates="solar_panels")
    # Relationship M:M with SolarSystem
    solar_systems = db.relationship("SolarSystem", secondary="solar_system_has_solar_panel",
                                    back_populates="solar_panels")

    __table_args__ = (
        Index('fk_solar_panel_energy_sale1_idx', 'energy_sale_id', 'energy_sale_electricity_price_id'),
        {},
    )

    def __repr__(self) -> str:
        return f"SolarPanel(id={self.id}, type='{self.type}', power={self.power}, is_tilt_angel={self.is_tilt_angel}, tilt_angle={self.tilt_angle}, time={self.time}, battery_charge={self.battery_charge}, energy_sale_id={self.energy_sale_id}, energy_sale_electricity_price_id={self.energy_sale_electricity_price_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "type": self.type,
            "power": self.power,
            "is_tilt_angel": self.is_tilt_angel,
            "tilt_angle": self.tilt_angle,
            "time": str(self.time),
            "battery_charge": self.battery_charge,
            "energy_sale_id": self.energy_sale_id,
            "energy_sale_electricity_price_id": self.energy_sale_electricity_price_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SolarPanel:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = SolarPanel(
            type=dto_dict.get("type"),
            power=dto_dict.get("power"),
            is_tilt_angel=dto_dict.get("is_tilt_angel"),
            tilt_angle=dto_dict.get("tilt_angle"),
            time=datetime.strptime(dto_dict.get("time"), "%H:%M:%S"),
            battery_charge=dto_dict.get("battery_charge"),
            energy_sale_id=dto_dict.get("energy_sale_id"),
            energy_sale_electricity_price_id=dto_dict.get("energy_sale_electricity_price_id"),
        )
        return obj
