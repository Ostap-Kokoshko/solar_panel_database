from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import installation_address_controller
from my_project.auth.domain import InstallationAddress

installation_address_bp = Blueprint('address', __name__, url_prefix='/address')


@installation_address_bp.get('/all')
def get_all_installation_address() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(installation_address_controller.find_all()), HTTPStatus.OK)


@installation_address_bp.post('')
def create_installation_address() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    installation_address = InstallationAddress.create_from_dto(content)
    installation_address_controller.create(installation_address)
    return make_response(jsonify(installation_address.put_into_dto()), HTTPStatus.CREATED)


@installation_address_bp.get('/<int:installation_address_id>')
def get_installation_address(installation_address_id: int) -> Response:
    """
    Gets installation_address by ID.
    :return: Response object
    """
    return make_response(jsonify(installation_address_controller.find_by_id(installation_address_id)), HTTPStatus.OK)


@installation_address_bp.put('/<int:installation_address_id>')
def update_installation_address(installation_address_id: int) -> Response:
    """
    Updates installation_address by ID.
    :return: Response object
    """
    content = request.get_json()
    installation_address = InstallationAddress.create_from_dto(content)
    installation_address_controller.update(installation_address_id, installation_address)
    return make_response("InstallationAddress updated", HTTPStatus.OK)


@installation_address_bp.patch('/<int:installation_address_id>')
def patch_installation_address(installation_address_id: int) -> Response:
    """
    Patches installation_address by ID.
    :return: Response object
    """
    content = request.get_json()
    installation_address_controller.patch(installation_address_id, content)
    return make_response("InstallationAddress updated", HTTPStatus.OK)


@installation_address_bp.delete('/<int:installation_address_id>')
def delete_installation_address(installation_address_id: int) -> Response:
    """
    Deletes installation_address by ID.
    :return: Response object
    """
    installation_address_controller.delete(installation_address_id)
    return make_response("InstallationAddress deleted", HTTPStatus.OK)
