from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import delivery_controller
from my_project.auth.domain import Delivery

delivery_bp = Blueprint('deliveries', __name__, url_prefix='/deliveries')


@delivery_bp.get('/all')
def get_all_delivery() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(delivery_controller.find_all()), HTTPStatus.OK)


@delivery_bp.post('')
def create_delivery() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_controller.create(delivery)
    return make_response(jsonify(delivery.put_into_dto()), HTTPStatus.CREATED)


@delivery_bp.post('/add_delivery')
def add_delivery() -> Response:
    content = request.get_json()
    name = content.get('name')
    price = content.get('price')

    if name is None or price is None:
        return make_response(jsonify({"error": "Name and price are required"}), HTTPStatus.BAD_REQUEST)

    try:
        delivery_controller.add_delivery(name, price)
        return make_response(jsonify({"message": "Delivery added successfully"}), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@delivery_bp.post('/insert_ten_deliveries')
def insert_ten_deliveries() -> Response:
    try:
        delivery_controller.insert_ten_deliveries()
        return make_response(jsonify({"message": "Ten deliveries added successfully"}), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@delivery_bp.post('/dynamic_table_creation')
def dynamic_table_creation() -> Response:
    try:
        delivery_controller.dynamic_table_creation()
        return make_response(jsonify({"message": "Dynamic tables created successfully"}), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@delivery_bp.get('/<int:delivery_id>')
def get_delivery(delivery_id: int) -> Response:
    """
    Gets delivery by ID.
    :return: Response object
    """
    return make_response(jsonify(delivery_controller.find_by_id(delivery_id)), HTTPStatus.OK)


@delivery_bp.get('/get_delivery_stats/<stat_type>')
def get_delivery_stats(stat_type: str) -> Response:
    return make_response(jsonify(delivery_controller.get_delivery_stats(stat_type)), HTTPStatus.OK)


@delivery_bp.put('/<int:delivery_id>')
def update_delivery(delivery_id: int) -> Response:
    """
    Updates delivery by ID.
    :return: Response object
    """
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_controller.update(delivery_id, delivery)
    return make_response("Delivery updated", HTTPStatus.OK)


@delivery_bp.patch('/<int:delivery_id>')
def patch_delivery(delivery_id: int) -> Response:
    """
    Patches delivery by ID.
    :return: Response object
    """
    content = request.get_json()
    delivery_controller.patch(delivery_id, content)
    return make_response("Delivery updated", HTTPStatus.OK)


@delivery_bp.delete('/<int:delivery_id>')
def delete_delivery(delivery_id: int) -> Response:
    """
    Deletes delivery by ID.
    :return: Response object
    """
    delivery_controller.delete(delivery_id)
    return make_response("Delivery deleted", HTTPStatus.OK)
