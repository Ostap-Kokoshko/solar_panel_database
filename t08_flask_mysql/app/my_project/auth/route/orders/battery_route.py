from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import battery_controller
from my_project.auth.domain import Battery

battery_bp = Blueprint('batteries', __name__, url_prefix='/batteries')


@battery_bp.get('/all')
def get_all_battery() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(battery_controller.find_all()), HTTPStatus.OK)


@battery_bp.get('/<int:battery_id>/solar_panels')
def get_all_batteries_from_solar_panels(battery_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(battery_controller.find_solar_panels(battery_id)), HTTPStatus.OK)


@battery_bp.post('')
def create_battery() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    battery = Battery.create_from_dto(content)
    battery_controller.create(battery)
    return make_response(jsonify(battery.put_into_dto()), HTTPStatus.CREATED)


@battery_bp.get('/<int:battery_id>')
def get_battery(battery_id: int) -> Response:
    """
    Gets battery by ID.
    :return: Response object
    """
    return make_response(jsonify(battery_controller.find_by_id(battery_id)), HTTPStatus.OK)


@battery_bp.post('/<int:battery_id>/add_panel')
def add_solar_panel_to_battery(battery_id) -> Response:
    try:
        data = request.get_json()
        solar_panel_id = data.get('solar_panel_id')

        battery_controller.add_solar_panel_to_battery(battery_id, solar_panel_id)

        return make_response(jsonify({"message": "Panel added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@battery_bp.put('/<int:battery_id>')
def update_battery(battery_id: int) -> Response:
    """
    Updates battery by ID.
    :return: Response object
    """
    content = request.get_json()
    battery = Battery.create_from_dto(content)
    battery_controller.update(battery_id, battery)
    return make_response("Battery updated", HTTPStatus.OK)


@battery_bp.patch('/<int:battery_id>/remove_panel')
def remove_battery_from_solar_panel(battery_id) -> Response:
    try:
        data = request.get_json()
        solar_panel_id = data.get('solar_panel_id')

        # Call the controller method to remove the battery from the solar panel
        battery_controller.remove_solar_panel_from_battery(battery_id, solar_panel_id)

        return make_response(jsonify({"message": "Panel removed successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@battery_bp.patch('/<int:battery_id>')
def patch_battery(battery_id: int) -> Response:
    """
    Patches battery by ID.
    :return: Response object
    """
    content = request.get_json()
    battery_controller.patch(battery_id, content)
    return make_response("Battery updated", HTTPStatus.OK)


@battery_bp.delete('/<int:battery_id>')
def delete_battery(battery_id: int) -> Response:
    """
    Deletes battery by ID.
    :return: Response object
    """
    battery_controller.delete(battery_id)
    return make_response("Battery deleted", HTTPStatus.OK)
