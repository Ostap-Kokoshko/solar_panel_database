from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import SolarPanel

from my_project.auth.domain.orders.battery import solar_panel_has_battery
from my_project.auth.domain.orders.battery import Battery

from my_project.auth.domain.orders.solar_system import solar_system_has_solar_panel
from my_project.auth.domain.orders.solar_system import SolarSystem


class SolarPanelDAO(GeneralDAO):
    """
    Realisation of SolarPanel data access layer.
    """
    _domain_type = SolarPanel

    def find_battery(self, solar_panel_id: int):
        """
        Find battery associated with a specific solar panel.
        :param solar_panel_id: ID of the solar_panel
        :return: List of Battery objects associated with the solar panel
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the bus IDs associated with the battery
        batteries_ids = (
            session.query(solar_panel_has_battery.c.battery_id)
            .filter(solar_panel_has_battery.c.solar_panel_id == solar_panel_id)
            .all()
        )

        # Extract solar panel IDs from the result
        battery_ids = [battery_id for (battery_id,) in batteries_ids]

        # Query the SolarPanel table to get the SolarPanel objects associated with the solar panel IDs
        batteries = session.query(Battery).filter(Battery.id.in_(battery_ids)).all()

        return [battery.put_into_dto() for battery in batteries]

    def solar_panel_find_solar_systems(self, solar_panel_id: int):
        """
        Find solar panel associated with a specific solar system.
        :param solar_panel_id: ID of the solar system
        :return: List of SolarPanel objects associated with the solar system
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the solar panel IDs associated with the solar system
        solar_systems_ids = (
            session.query(solar_system_has_solar_panel.c.solar_system_id)
            .filter(solar_system_has_solar_panel.c.solar_panel_id == solar_panel_id)
            .all()
        )

        # Extract solar system IDs from the result
        solar_system_ids = [solar_system_id for (solar_system_id,) in solar_systems_ids]

        # Query the SolarSystem table to get the SolarSystem objects associated with the solar system IDs
        solar_systems = session.query(SolarSystem).filter(SolarSystem.id.in_(solar_system_ids)).all()

        return [solar_system.put_into_dto() for solar_system in solar_systems]
