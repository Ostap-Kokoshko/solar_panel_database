from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import order_controller
from my_project.auth.domain import Order

order_bp = Blueprint('orders', __name__, url_prefix='/orders')


@order_bp.get('/all')
def get_all_orders() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(order_controller.find_all()), HTTPStatus.OK)


@order_bp.get('/<int:order_id>/solar_systems')
def get_all_orders_from_solar_systems(order_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(order_controller.find_solar_systems(order_id)), HTTPStatus.OK)


@order_bp.post('')
def create_order() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    order = Order.create_from_dto(content)
    order_controller.create(order)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.CREATED)


@order_bp.get('/<int:order_id>')
def get_order(order_id: int) -> Response:
    """
    Gets order by ID.
    :return: Response object
    """
    return make_response(jsonify(order_controller.find_by_id(order_id)), HTTPStatus.OK)


@order_bp.put('/<int:order_id>')
def update_order(order_id: int) -> Response:
    """
    Updates order by ID.
    :return: Response object
    """
    content = request.get_json()
    order = Order.create_from_dto(content)
    order_controller.update(order_id, order)
    return make_response("Order updated", HTTPStatus.OK)


@order_bp.patch('/<int:order_id>')
def patch_order(order_id: int) -> Response:
    """
    Patches order by ID.
    :return: Response object
    """
    content = request.get_json()
    order_controller.patch(order_id, content)
    return make_response("Order updated", HTTPStatus.OK)


@order_bp.delete('/<int:order_id>')
def delete_order(order_id: int) -> Response:
    """
    Deletes order by ID.
    :return: Response object
    """
    order_controller.delete(order_id)
    return make_response("Order deleted", HTTPStatus.OK)
