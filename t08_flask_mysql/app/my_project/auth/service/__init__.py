from .orders.client_service import ClientService
from .orders.battery_service import BatteryService
from .orders.city_service import CityService
from .orders.delivery_service import DeliveryService
from .orders.electricity_price_service import ElectricityPriceService
from .orders.energy_sale_service import EnergySaleService
from .orders.installation_address_service import InstallationAddressService
from .orders.order_service import OrderService
from .orders.owner_service import OwnerService
from .orders.region_service import RegionService
from .orders.solar_panel_service import SolarPanelService
from .orders.solar_system_service import SolarSystemService

client_service = ClientService()
battery_service = BatteryService()
city_service = CityService()
delivery_service = DeliveryService()
electricity_price_service = ElectricityPriceService()
energy_sale_service = EnergySaleService()
installation_address_service = InstallationAddressService()
order_service = OrderService()
owner_service = OwnerService()
region_service = RegionService()
solar_panel_service = SolarPanelService()
solar_system_service = SolarSystemService()
