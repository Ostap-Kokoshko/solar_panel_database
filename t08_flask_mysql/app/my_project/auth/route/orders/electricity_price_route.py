from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import electricity_price_controller
from my_project.auth.domain import ElectricityPrice

electricity_price_bp = Blueprint('electro-price', __name__, url_prefix='/electro-price')


@electricity_price_bp.get('/all')
def get_all_electricity_price() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(electricity_price_controller.find_all()), HTTPStatus.OK)


@electricity_price_bp.post('')
def create_electricity_price() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    electricity_price = ElectricityPrice.create_from_dto(content)
    electricity_price_controller.create(electricity_price)
    return make_response(jsonify(electricity_price.put_into_dto()), HTTPStatus.CREATED)


@electricity_price_bp.get('/<int:electricity_price_id>')
def get_electricity_price(electricity_price_id: int) -> Response:
    """
    Gets electricity_price by ID.
    :return: Response object
    """
    return make_response(jsonify(electricity_price_controller.find_by_id(electricity_price_id)), HTTPStatus.OK)


@electricity_price_bp.put('/<int:electricity_price_id>')
def update_electricity_price(electricity_price_id: int) -> Response:
    """
    Updates electricity_price by ID.
    :return: Response object
    """
    content = request.get_json()
    electricity_price = ElectricityPrice.create_from_dto(content)
    electricity_price_controller.update(electricity_price_id, electricity_price)
    return make_response("ElectricityPrice updated", HTTPStatus.OK)


@electricity_price_bp.patch('/<int:electricity_price_id>')
def patch_electricity_price(electricity_price_id: int) -> Response:
    """
    Patches electricity_price by ID.
    :return: Response object
    """
    content = request.get_json()
    electricity_price_controller.patch(electricity_price_id, content)
    return make_response("ElectricityPrice updated", HTTPStatus.OK)


@electricity_price_bp.delete('/<int:electricity_price_id>')
def delete_electricity_price(electricity_price_id: int) -> Response:
    """
    Deletes electricity_price by ID.
    :return: Response object
    """
    electricity_price_controller.delete(electricity_price_id)
    return make_response("ElectricityPrice deleted", HTTPStatus.OK)
