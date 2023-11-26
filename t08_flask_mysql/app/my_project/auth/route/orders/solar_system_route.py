from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import solar_system_controller
from my_project.auth.domain import SolarSystem

solar_system_bp = Blueprint('solar_systems', __name__, url_prefix='/solar_systems')


@solar_system_bp.get('/all')
def get_all_solar_systems() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(solar_system_controller.find_all()), HTTPStatus.OK)


@solar_system_bp.get('/<int:solar_system_id>/solar_system_panels')
def get_all_solar_systems_from_solar_panels(solar_system_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(solar_system_controller.solar_system_find_solar_panels(solar_system_id)),
                         HTTPStatus.OK)


@solar_system_bp.get('/<int:solar_system_id>/solar_system_orders')
def get_all_solar_systems_from_orders(solar_system_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(solar_system_controller.find_orders(solar_system_id)), HTTPStatus.OK)


@solar_system_bp.get('/<int:solar_system_id>/solar_system_owners')
def get_all_solar_systems_from_owners(solar_system_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(solar_system_controller.find_owners(solar_system_id)), HTTPStatus.OK)


@solar_system_bp.post('')
def create_solar_system() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    solar_system = SolarSystem.create_from_dto(content)
    solar_system_controller.create(solar_system)
    return make_response(jsonify(solar_system.put_into_dto()), HTTPStatus.CREATED)


@solar_system_bp.get('/<int:solar_system_id>')
def get_solar_system(solar_system_id: int) -> Response:
    """
    Gets SolarSystem by ID.
    :return: Response object
    """
    return make_response(jsonify(solar_system_controller.find_by_id(solar_system_id)), HTTPStatus.OK)


@solar_system_bp.put('/<int:solar_system_id>')
def update_solar_system(solar_system_id: int) -> Response:
    """
    Updates SolarSystem by ID.
    :return: Response object
    """
    content = request.get_json()
    solar_system = SolarSystem.create_from_dto(content)
    solar_system_controller.update(solar_system_id, solar_system)
    return make_response("SolarSystem updated", HTTPStatus.OK)


@solar_system_bp.patch('/<int:solar_system_id>')
def patch_solar_system(solar_system_id: int) -> Response:
    """
    Patches SolarSystem by ID.
    :return: Response object
    """
    content = request.get_json()
    solar_system_controller.patch(solar_system_id, content)
    return make_response("SolarSystem updated", HTTPStatus.OK)


@solar_system_bp.delete('/<int:solar_system_id>')
def delete_solar_system(solar_system_id: int) -> Response:
    """
    Deletes SolarSystem by ID.
    :return: Response object
    """
    solar_system_controller.delete(solar_system_id)
    return make_response("SolarSystem deleted", HTTPStatus.OK)
