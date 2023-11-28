from __future__ import annotations

from datetime import datetime
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy import DECIMAL

order_has_solar_system = db.Table(
    'order_has_solar_system',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('solar_system_id', db.Integer, db.ForeignKey('solar_system.id'), primary_key=True),
    db.UniqueConstraint('order_id', 'solar_system_id', name='uq_order_has_solar_system'),
    extend_existing=True
)


class Order(db.Model, IDto):
    """
    Model declaration for Order.
    """
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.id'), nullable=False)
    is_delivery = db.Column(db.Boolean, nullable=False)
    delivery_time = db.Column(db.DateTime, nullable=True)
    street_address = db.Column(db.String(45), nullable=True)
    total_price = db.Column(db.DECIMAL, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    city_region_name = db.Column(db.String(50), db.ForeignKey('region.name'), nullable=False)

    # Relationships
    client = db.relationship("Client", backref="orders_clients")
    delivery = db.relationship("Delivery", backref="orders_deliveries")
    city = db.relationship("City", backref="orders_cities")

    # Relationship M:M with SolarSystem
    solar_systems = db.relationship("SolarSystem", secondary="order_has_solar_system", back_populates="orders")

    def __repr__(self) -> str:
        return f"Order(id={self.id}, client_id={self.client_id}, delivery_id={self.delivery_id}, is_delivery={self.is_delivery}, delivery_time={self.delivery_time}, street_address='{self.street_address}', total_price={self.total_price}, city_id={self.city_id}, city_region_name='{self.city_region_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "client_id": self.client_id,
            "delivery_id": self.delivery_id,
            "is_delivery": self.is_delivery,
            "delivery_time": str(self.delivery_time) if self.delivery_time else "",
            "street_address": self.street_address,
            "total_price": str(self.total_price),
            "city_id": self.city_id,
            "city_region_name": self.city_region_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Order:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Order(
            client_id=dto_dict.get("client_id"),
            delivery_id=dto_dict.get("delivery_id"),
            is_delivery=dto_dict.get("is_delivery"),
            delivery_time=datetime.strptime(dto_dict.get("delivery_time"), "%Y-%m-%d %H:%M:%S") if dto_dict.get("delivery_time") else None,
            street_address=dto_dict.get("street_address"),
            total_price=dto_dict.get("total_price"),
            city_id=dto_dict.get("city_id"),
            city_region_name=dto_dict.get("city_region_name"),
        )
        return obj
