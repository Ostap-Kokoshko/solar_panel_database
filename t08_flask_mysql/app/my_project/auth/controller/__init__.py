from .orders.client_controller import ClientController
from .orders.battery_controller import BatteryController
from .orders.city_controller import CityController
from .orders.delivery_controller import DeliveryController
from .orders.electricity_price_controller import ElectricityPriceController
from .orders.energy_sale_controller import EnergySaleController
from .orders.installation_address_controller import InstallationAddressController
from .orders.order_controller import OrderController
from .orders.owner_controller import OwnerController
from .orders.region_controller import RegionController
from .orders.solar_panel_controller import SolarPanelController
from .orders.solar_system_controller import SolarSystemController

client_controller = ClientController()
battery_controller = BatteryController()
city_controller = CityController()
delivery_controller = DeliveryController()
electricity_price_controller = ElectricityPriceController()
energy_sale_controller = EnergySaleController()
installation_address_controller = InstallationAddressController()
order_controller = OrderController()
owner_controller = OwnerController()
region_controller = RegionController()
solar_panel_controller = SolarPanelController()
solar_system_controller = SolarSystemController()
