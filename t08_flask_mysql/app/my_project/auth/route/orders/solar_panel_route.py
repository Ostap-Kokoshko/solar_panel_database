from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import solar_panel_controller
from my_project.auth.domain import SolarPanel

solar_panel_bp = Blueprint('panels', __name__, url_prefix='/panels')


@solar_panel_bp.get('/all')
def get_all_panels() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(solar_panel_controller.find_all()), HTTPStatus.OK)


@solar_panel_bp.get('/<int:solar_panel_id>/solar_panel_batteries')
def get_all_batteries_from_solar_panels(solar_panel_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(solar_panel_controller.find_battery(solar_panel_id)), HTTPStatus.OK)


@solar_panel_bp.get('/<int:solar_panel_id>/solar_panel_systems')
def get_all_solar_panels_from_solar_systems(solar_panel_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(solar_panel_controller.solar_panel_find_solar_systems(solar_panel_id)), HTTPStatus.OK)


@solar_panel_bp.get('/all/solar_panel_systems')
def get_all_panels_and_systems() -> Response:
    """
    Gets all solar panels and solar systems using Service layer.
    :return: Response object
    """
    solar_panels_and_systems = solar_panel_controller.find_all_panels_and_systems()

    return make_response(jsonify(solar_panels_and_systems), HTTPStatus.OK)


@solar_panel_bp.get('/all/solar_panel_batteries')
def get_all_panels_with_batteries() -> Response:
    """
    Gets all solar panels with their associated batteries using Service layer.
    :return: Response object
    """
    panels_with_batteries = solar_panel_controller.find_all_panels_with_batteries()

    return make_response(jsonify(panels_with_batteries), HTTPStatus.OK)


@solar_panel_bp.post('/<int:solar_panel_id>/add_battery')
def add_battery_to_solar_panel(solar_panel_id) -> Response:
    """
    Adds a battery to a specific solar panel.
    :param solar_panel_id: ID of the solar panel
    :return: Response object
    """
    try:
        # Get the battery_id from the request payload
        data = request.get_json()
        battery_id = data.get('battery_id')

        # Call the controller method to add the battery to the solar panel
        solar_panel_controller.add_battery_to_solar_panel(solar_panel_id, battery_id)

        return make_response(jsonify({"message": "Battery added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@solar_panel_bp.post('')
def create_solar_panel() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    solar_panel = SolarPanel.create_from_dto(content)
    solar_panel_controller.create(solar_panel)
    return make_response(jsonify(solar_panel.put_into_dto()), HTTPStatus.CREATED)


@solar_panel_bp.get('/<int:solar_panel_id>')
def get_solar_panel(solar_panel_id: int) -> Response:
    """
    Gets SolarPanel by ID.
    :return: Response object
    """
    return make_response(jsonify(solar_panel_controller.find_by_id(solar_panel_id)), HTTPStatus.OK)


@solar_panel_bp.put('/<int:solar_panel_id>')
def update_solar_panel(solar_panel_id: int) -> Response:
    """
    Updates SolarPanel by ID.
    :return: Response object
    """
    content = request.get_json()
    solar_panel = SolarPanel.create_from_dto(content)
    solar_panel_controller.update(solar_panel_id, solar_panel)
    return make_response("SolarPanel updated", HTTPStatus.OK)


@solar_panel_bp.patch('/<int:solar_panel_id>/remove_battery')
def remove_battery_from_solar_panel(solar_panel_id) -> Response:
    """
    Removes a battery from a specific solar panel.
    :param solar_panel_id: ID of the solar panel
    :return: Response object
    """
    try:
        # Get the battery_id from the request payload
        data = request.get_json()
        battery_id = data.get('battery_id')

        # Call the controller method to remove the battery from the solar panel
        solar_panel_controller.remove_battery_from_solar_panel(solar_panel_id, battery_id)

        return make_response(jsonify({"message": "Battery removed successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@solar_panel_bp.patch('/<int:solar_panel_id>')
def patch_solar_panel(solar_panel_id: int) -> Response:
    """
    Patches SolarPanel by ID.
    :return: Response object
    """
    content = request.get_json()
    solar_panel_controller.patch(solar_panel_id, content)
    return make_response("SolarPanel updated", HTTPStatus.OK)


@solar_panel_bp.delete('/<int:solar_panel_id>')
def delete_solar_panel(solar_panel_id: int) -> Response:
    """
    Deletes SolarPanel by ID.
    :return: Response object
    """
    solar_panel_controller.delete(solar_panel_id)
    return make_response("SolarPanel deleted", HTTPStatus.OK)
