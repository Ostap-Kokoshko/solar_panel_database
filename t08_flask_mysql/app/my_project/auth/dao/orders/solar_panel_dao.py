from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import SolarPanel

from my_project.auth.domain.orders.battery import solar_panel_has_battery
from my_project.auth.domain.orders.battery import Battery

from my_project.auth.domain.orders.solar_system import solar_system_has_solar_panel
from my_project.auth.domain.orders.solar_system import SolarSystem

from sqlalchemy.orm import joinedload


class SolarPanelDAO(GeneralDAO):
    """
    Realisation of SolarPanel data access layer.
    """
    _domain_type = SolarPanel

    def find_battery(self, solar_panel_id: int):
        """
        Find solar panel and its associated batteries.
        :param solar_panel_id: ID of the solar_panel
        :return: Dictionary containing information about the solar panel and its batteries
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the SolarPanel table to get the SolarPanel object
        solar_panel = session.query(SolarPanel).filter_by(id=solar_panel_id).first()

        # Query the association table to get the battery IDs associated with the solar panel
        battery_ids = (
            session.query(solar_panel_has_battery.c.battery_id)
            .filter(solar_panel_has_battery.c.solar_panel_id == solar_panel_id)
            .all()
        )

        # Extract battery IDs from the result
        battery_ids = [battery_id for (battery_id,) in battery_ids]

        # Query the Battery table to get the Battery objects associated with the battery IDs
        batteries = session.query(Battery).filter(Battery.id.in_(battery_ids)).all()

        # Create a dictionary to store information about the solar panel and its batteries
        solar_panel_data = {
            "solar_panel": solar_panel.put_into_dto(),
            "batteries": [battery.put_into_dto() for battery in batteries]
        }

        return solar_panel_data

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

    def find_all_solar_systems(self):
        """
        Find all solar systems.
        :return: List of SolarSystem objects
        """
        session = self.get_session()
        return session.query(SolarSystem).all()

    def find_all_batteries(self):
        session = self.get_session()
        return session.query(Battery).all()

    def add_battery_to_solar_panel(self, solar_panel_id: int, battery_id: int):
        session = self.get_session()

        association = solar_panel_has_battery.insert().values(
            solar_panel_id=solar_panel_id,
            battery_id=battery_id
        )

        session.execute(association)

        session.commit()

    def remove_battery_from_solar_panel(self, solar_panel_id: int, battery_id: int):
        """
        Removes a battery from a specific solar panel in the database.
        :param solar_panel_id: ID of the solar panel
        :param battery_id: ID of the battery
        :return: None
        """
        session = self.get_session()

        # Delete the association from the solar_panel_has_battery table
        session.execute(
            solar_panel_has_battery.delete()
            .where(solar_panel_has_battery.c.solar_panel_id == solar_panel_id)
            .where(solar_panel_has_battery.c.battery_id == battery_id)
        )

        session.commit()

    def find_by_id_with_batteries(self, solar_panel_id: int):
        """
        Finds a solar panel by ID with information about connected batteries.
        :param solar_panel_id: ID of the solar panel
        :return: SolarPanel object with connected batteries
        """
        session = self.get_session()

        solar_panel = (
            session.query(SolarPanel)
            .options(joinedload(SolarPanel.batteries))
            .filter(SolarPanel.id == solar_panel_id)
            .first()
        )

        return solar_panel
