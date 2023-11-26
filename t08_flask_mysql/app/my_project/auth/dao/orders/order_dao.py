from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Order

from my_project.auth.domain.orders.solar_system import order_has_solar_system
from my_project.auth.domain.orders.solar_system import SolarSystem


class OrderDAO(GeneralDAO):
    """
    Realisation of Order data access layer.
    """
    _domain_type = Order

    def find_solar_systems(self, order_id: int):
        """
        Find solar system associated with a specific order.
        :param order_id: ID of the order
        :return: List of SolarSystem objects associated with the order
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the solar system IDs associated with the order
        solar_systems_ids = (
            session.query(order_has_solar_system.c.solar_system_id)
            .filter(order_has_solar_system.c.order_id == order_id)
            .all()
        )

        # Extract solar system IDs from the result
        solar_system_ids = [solar_system_id for (solar_system_id,) in solar_systems_ids]

        # Query the SolarSystem table to get the SolarSystem objects associated with the solar system IDs
        solar_systems = session.query(SolarSystem).filter(SolarSystem.id.in_(solar_system_ids)).all()

        return [solar_system.put_into_dto() for solar_system in solar_systems]
