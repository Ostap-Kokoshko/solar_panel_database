from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import region_controller
from my_project.auth.domain import Region

region_bp = Blueprint('regions', __name__, url_prefix='/regions')


@region_bp.get('/all')
def get_all_regions() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(region_controller.find_all()), HTTPStatus.OK)


@region_bp.post('')
def create_region() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    region = Region.create_from_dto(content)
    region_controller.create(region)
    return make_response(jsonify(region.put_into_dto()), HTTPStatus.CREATED)


@region_bp.get('/<string:region_name>')
def get_region(region_name: str) -> Response:
    """
    Gets region by ID.
    :return: Response object
    """
    return make_response(jsonify(region_controller.find_by_id(region_name)), HTTPStatus.OK)


@region_bp.put('/<string:region_name>')
def update_region(region_name: str) -> Response:
    """
    Updates region by ID.
    :return: Response object
    """
    content = request.get_json()
    region = Region.create_from_dto(content)
    region_controller.update(region_name, region)
    return make_response("Region updated", HTTPStatus.OK)


@region_bp.patch('/<string:region_name>')
def patch_region(region_name: str) -> Response:
    """
    Patches region by ID.
    :return: Response object
    """
    content = request.get_json()
    region_controller.patch(region_name, content)
    return make_response("Region updated", HTTPStatus.OK)


@region_bp.delete('/<string:region_name>')
def delete_region(region_name: str) -> Response:
    """
    Deletes region by ID.
    :return: Response object
    """
    region_controller.delete(region_name)
    return make_response("Region deleted", HTTPStatus.OK)
