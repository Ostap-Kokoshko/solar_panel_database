from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import SolarSystem

from my_project.auth.domain.orders.solar_panel import solar_system_has_solar_panel
from my_project.auth.domain.orders.solar_panel import SolarPanel

from my_project.auth.domain.orders.order import order_has_solar_system
from my_project.auth.domain.orders.order import Order

from my_project.auth.domain.orders.owner import owner_solar_system
from my_project.auth.domain.orders.owner import Owner


class SolarSystemDAO(GeneralDAO):
    """
    Realisation of SolarSystem data access layer.
    """
    _domain_type = SolarSystem

    def solar_system_find_solar_panels(self, solar_system_id: int):
        """
        Find solar system associated with a specific solar panel.
        :param solar_system_id: ID of the solar panel
        :return: List of SolarSystem objects associated with the solar panel
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the solar system IDs associated with the solar panel
        solar_panels_ids = (
            session.query(solar_system_has_solar_panel.c.solar_panel_id)
            .filter(solar_system_has_solar_panel.c.solar_system_id == solar_system_id)
            .all()
        )

        # Extract solar panel IDs from the result
        solar_panel_ids = [solar_system_id for (solar_system_id,) in solar_panels_ids]

        # Query the SolarPanel table to get the SolarPanel objects associated with the solar panel IDs
        solar_panels = session.query(SolarPanel).filter(SolarPanel.id.in_(solar_panel_ids)).all()

        return [solar_panel.put_into_dto() for solar_panel in solar_panels]

    def find_orders(self, solar_system_id: int):
        """
        Find order associated with a specific solar system.
        :param solar_system_id: ID of the solar system
        :return: List of Order objects associated with the solar system
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the order IDs associated with the solar system
        orders_ids = (
            session.query(order_has_solar_system.c.order_id)
            .filter(order_has_solar_system.c.solar_system_id == solar_system_id)
            .all()
        )

        # Extract order IDs from the result
        order_ids = [order_id for (order_id,) in orders_ids]

        # Query the Order table to get the Order objects associated with the order IDs
        orders = session.query(Order).filter(Order.id.in_(order_ids)).all()

        return [order.put_into_dto() for order in orders]

    def find_owners(self, solar_system_id: int):
        """
        Find owner associated with a specific solar system.
        :param solar_system_id: ID of the solar system
        :return: List of Owner objects associated with the solar system
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the owner IDs associated with the solar system
        owners_ids = (
            session.query(owner_solar_system.c.owner_id)
            .filter(owner_solar_system.c.solar_system_id == solar_system_id)
            .all()
        )

        # Extract owner IDs from the result
        owner_ids = [owner_id for (owner_id,) in owners_ids]

        # Query the Owner table to get the Owner objects associated with the owner IDs
        owners = session.query(Owner).filter(Owner.id.in_(owner_ids)).all()

        return [owner.put_into_dto() for owner in owners]

