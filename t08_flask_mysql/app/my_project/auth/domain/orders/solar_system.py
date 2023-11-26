from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy import UniqueConstraint, Index

order_has_solar_system = db.Table(
    'order_has_solar_system',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('solar_system_id', db.Integer, db.ForeignKey('solar_system.id'), primary_key=True),
    db.UniqueConstraint('order_id', 'solar_system_id', name='uq_order_has_solar_system'),
    extend_existing=True
)

owner_solar_system = db.Table(
    'owner_solar_system',
    db.Column('owner_id', db.Integer, db.ForeignKey('owner.id'), primary_key=True),
    db.Column('solar_system_id', db.Integer, db.ForeignKey('solar_system.id'), primary_key=True),
    db.UniqueConstraint('owner_id', 'solar_system_id', name='uq_owner_solar_system'),
    extend_existing=True
)

solar_system_has_solar_panel = db.Table(
    'solar_system_has_solar_panel',
    db.Column('solar_system_id', db.Integer, db.ForeignKey('solar_system.id'), primary_key=True),
    db.Column('solar_panel_id', db.Integer, db.ForeignKey('solar_panel.id'), primary_key=True),
    db.UniqueConstraint('solar_system_id', 'solar_panel_id', name='uq_solar_system_has_solar_panel'),
    extend_existing=True
)


class SolarSystem(db.Model, IDto):
    """
    Model declaration for SolarSystem.
    """
    __tablename__ = "solar_system"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    battery_capacity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.DECIMAL, nullable=False)
    installation_address_id = db.Column(db.Integer, db.ForeignKey('installation_address.id'), nullable=False)
    installation_address_city_id = db.Column(db.Integer, db.ForeignKey('installation_address_city.id'), nullable=False)
    installation_address_city_region_name = db.Column(db.String(50),
                                                      db.ForeignKey('installation_address_city_region.name'),
                                                      nullable=False)

    # Relationship M:1 with InstallationAddress
    installation_address = db.relationship("InstallationAddress", backref="solar_systems")
    owners = db.relationship("Owner", secondary="owner_solar_system", back_populates="solar_systems")
    # Relationship M:M with Order
    orders = db.relationship("Order", secondary="order_has_solar_system", back_populates="solar_systems")
    # Relationship M:M with SolarPanel
    solar_panels = db.relationship("SolarPanel", secondary="solar_system_has_solar_panel",
                                   back_populates="solar_systems")

    __table_args__ = (
        UniqueConstraint('id', 'installation_address_id', 'installation_address_city_id',
                         'installation_address_city_region_name'),
        Index('fk_solar_system_installation_address1_idx', 'installation_address_id', 'installation_address_city_id',
              'installation_address_city_region_name'),
        {},
    )

    def __repr__(self) -> str:
        return f"SolarSystem({self.id}, '{self.name}', {self.battery_capacity}, {self.price}, '{self.installation_address.street}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "battery_capacity": self.battery_capacity,
            "price": str(self.price),
            "installation_address_id": self.installation_address_id,
            "installation_address_city_id": self.installation_address_city_id,
            "installation_address_city_region_name": self.installation_address_city_region_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SolarSystem:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = SolarSystem(
            name=dto_dict.get("name"),
            battery_capacity=dto_dict.get("battery_capacity"),
            price=dto_dict.get("price"),
            installation_address_id=dto_dict.get("installation_address_id"),
            installation_address_city_id=dto_dict.get("installation_address_city_id"),
            installation_address_city_region_name=dto_dict.get("installation_address_city_region_name"),
        )
        return obj
