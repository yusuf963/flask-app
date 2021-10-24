from flask import Flask, request, jsonify
from models.data_users import users_db

router = Flask("user", __name__)


@router.route("/users", methods=['GET'])
def get_all_user():
    return jsonify(users_db), 200


@router.route("/user", methods=["POST"])
def create_user():
    return jsonify(users_db), 200


@router.route("/dial/<int:id>", methods=["GET"])
def get_single_user(user_id):
    filtered_users = list(
        filter(lambda user: user['id'] == user_id, users_db['']))
    return jsonify(users_db), 200


@router.route("/dial/<int:id>", methods=["UPDATE"])
def update_users():
    return jsonify(users_db), 200


@router.route("/dial/<int:id>", methods=["DELETE"])
def delete_users(id):
    return jsonify(id), 200
