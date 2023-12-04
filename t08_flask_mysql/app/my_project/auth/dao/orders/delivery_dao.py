from sqlalchemy import text

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Delivery


class DeliveryDAO(GeneralDAO):
    """
    Realisation of Delivery data access layer.
    """
    _domain_type = Delivery

    # STORED PROCEDURES
    def insert_into_delivery(self, in_name: str, in_price: int):
        """
        Insert a new delivery record into the database.
        """
        try:
            session = self.get_session()

            sql_expression = text("CALL insert_into_delivery(:name, :price)")
            session.execute(sql_expression, {'name': in_name, 'price': in_price})

            session.commit()
        except Exception as e:
            print(f"Error inserting into delivery: {e}")

    def insert_ten_into_delivery(self):
        """
        Insert ten delivery records into the database.
        """
        try:
            session = self.get_session()
            sql_expression = text("CALL insert_ten_into_delivery()")
            session.execute(sql_expression)
            session.commit()
        except Exception as e:
            print(f"Error inserting ten deliveries: {e}")

    def get_delivery_stats(self, stat_type: str):
        try:
            session = self.get_session()
            sql_expression = text("SELECT get_delivery_stats(:stat_type) AS result")
            result = session.execute(sql_expression, {'stat_type': stat_type}).scalar()
            return result
        except Exception as e:
            print(f"Error getting delivery stats: {e}")
            return None
