from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.client_route import client_bp
    from .orders.battery_route import battery_bp
    from .orders.city_route import city_bp
    from .orders.delivery_route import delivery_bp
    from .orders.electricity_price_route import electricity_price_bp
    from .orders.energy_sale_route import energy_sale_bp
    from .orders.installation_address_route import installation_address_bp
    from .orders.order_route import order_bp
    from .orders.owner_route import owner_bp
    from .orders.region_route import region_bp
    from .orders.solar_panel_route import solar_panel_bp
    from .orders.solar_system_route import solar_system_bp

    app.register_blueprint(client_bp)
    app.register_blueprint(battery_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(delivery_bp)
    app.register_blueprint(electricity_price_bp)
    app.register_blueprint(energy_sale_bp)
    app.register_blueprint(installation_address_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(owner_bp)
    app.register_blueprint(region_bp)
    app.register_blueprint(solar_panel_bp)
    app.register_blueprint(solar_system_bp)
