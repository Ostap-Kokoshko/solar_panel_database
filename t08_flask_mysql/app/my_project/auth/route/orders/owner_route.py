from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import owner_controller
from my_project.auth.domain import Owner

owner_bp = Blueprint('owners', __name__, url_prefix='/owners')


@owner_bp.get('/all')
def get_all_owners() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(owner_controller.find_all()), HTTPStatus.OK)


@owner_bp.get('/<int:owner_id>/owner_solar_systems')
def get_all_owners_from_solar_systems(owner_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(owner_controller.owner_find_solar_systems(owner_id)), HTTPStatus.OK)


@owner_bp.post('')
def create_owner() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.create(owner)
    return make_response(jsonify(owner.put_into_dto()), HTTPStatus.CREATED)


@owner_bp.get('/<int:owner_id>')
def get_owner(owner_id: int) -> Response:
    """
    Gets owner by ID.
    :return: Response object
    """
    return make_response(jsonify(owner_controller.find_by_id(owner_id)), HTTPStatus.OK)


@owner_bp.put('/<int:owner_id>')
def update_owner(owner_id: int) -> Response:
    """
    Updates owner by ID.
    :return: Response object
    """
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.update(owner_id, owner)
    return make_response("Owner updated", HTTPStatus.OK)


@owner_bp.patch('/<int:owner_id>')
def patch_owner(owner_id: int) -> Response:
    """
    Patches owner by ID.
    :return: Response object
    """
    content = request.get_json()
    owner_controller.patch(owner_id, content)
    return make_response("Owner updated", HTTPStatus.OK)


@owner_bp.delete('/<int:owner_id>')
def delete_owner(owner_id: int) -> Response:
    """
    Deletes owner by ID.
    :return: Response object
    """
    owner_controller.delete(owner_id)
    return make_response("Owner deleted", HTTPStatus.OK)
