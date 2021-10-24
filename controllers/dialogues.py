from flask import Blueprint, request, jsonify
from models.data_dialogues import dialouges_db


router = Blueprint("dialogues", __name__)


@router.route("/dial", methods=["GET"])
def get_dialouges():
    return jsonify(dialouges_db), 200


@router.route("/dial", methods=["POST"])
def create_dialouges():
    return jsonify('stuff posted', dialouges_db), 200


@router.route("/dial/<int:dial_id>", methods=["GET"])
def get_single_dailouges(dial_id):
    return jsonify(f'the id is {dial_id}', dialouges_db), 200


@router.route("/dial/<int:dial_id>", methods=["PATCH"])
def update_dialouges(dial_id):
    return jsonify(f'the id is {dial_id}',  dial_id), 200


@router.route("/dial/<int:dial_id>", methods=["DELETE"])
def delete_dialouges(dial_id):
    return jsonify(f'the id is {dial_id}', dial_id), 200
