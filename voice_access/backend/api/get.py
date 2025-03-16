from flask import jsonify, request
from . import api_bp

ret = [
    {"id": 1},
    {"id": 2},
]

@api_bp.route("/get", methods=["GET"])
def get():
    return jsonify(ret)