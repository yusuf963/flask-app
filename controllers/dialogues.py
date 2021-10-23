from flask import Blueprint, request, jsonify
from models.data_dialogues import dialouges_db
from models.data_users import users_db


router = Blueprint("dialogues", __name__)


@router.route("/dial", methods=["GET"])
def get_dialouges():
    return jsonify(dialouges_db), 200


@router.route("/dial", methods=["POST"])
def get_dialouges():
    return jsonify(dialouges_db), 200


@router.route("/dial/<int:id>", methods=["GET"])
def get_single_ialouges():
    return jsonify(dialouges_db), 200


@router.route("/dial/<int:id>", methods=["UPDATE"])
def update_dialouges():
    return jsonify(dialouges_db), 200


@router.route("/dial/<int:id>", methods=["DELETE"])
def delete_dialouges(id):
    return jsonify(id), 200
