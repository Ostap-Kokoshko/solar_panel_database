from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Battery

from my_project.auth.domain.orders.solar_panel import solar_panel_has_battery
from my_project.auth.domain.orders.solar_panel import SolarPanel


class BatteryDAO(GeneralDAO):
    """
    Realisation of Battery data access layer.
    """
    _domain_type = Battery

    def find_solar_panels(self, battery_id: int):
        """
        Find solar panel associated with a specific battery.
        :param battery_id: ID of the battery
        :return: List of SolarPanel objects associated with the battery
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the solar panel IDs associated with the battery
        solar_panels_ids = (
            session.query(solar_panel_has_battery.c.solar_panel_id)
            .filter(solar_panel_has_battery.c.battery_id == battery_id)
            .all()
        )

        # Extract solar panel IDs from the result
        solar_panel_ids = [solar_panel_id for (solar_panel_id,) in solar_panels_ids]

        # Query the SolarPanel table to get the SolarPanel objects associated with the solar panel IDs
        solar_panels = session.query(SolarPanel).filter(SolarPanel.id.in_(solar_panel_ids)).all()

        return [solar_panel.put_into_dto() for solar_panel in solar_panels]
