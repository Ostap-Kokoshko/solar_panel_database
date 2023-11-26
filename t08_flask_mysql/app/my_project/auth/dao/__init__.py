from .orders.client_dao import ClientDAO
from .orders.battery_dao import BatteryDAO
from .orders.city_dao import CityDAO
from .orders.delivery_dao import DeliveryDAO
from .orders.electricity_price_dao import ElectricityPriceDAO
from .orders.energy_sale_dao import EnergySaleDAO
from .orders.installation_address_dao import InstallationAddressDAO
from .orders.order_dao import OrderDAO
from .orders.owner_dao import OwnerDAO
from .orders.region_dao import RegionDAO
from .orders.solar_panel_dao import SolarPanelDAO
from .orders.solar_system_dao import SolarSystemDAO

client_dao = ClientDAO()
battery_dao = BatteryDAO()
city_dao = CityDAO()
delivery_dao = DeliveryDAO()
electricity_price_dao = ElectricityPriceDAO()
energy_sale_dao = EnergySaleDAO()
installation_address_dao = InstallationAddressDAO()
order_dao = OrderDAO()
owner_dao = OwnerDAO()
region_dao = RegionDAO()
solar_panel_dao = SolarPanelDAO()
solar_system_dao = SolarSystemDAO()
