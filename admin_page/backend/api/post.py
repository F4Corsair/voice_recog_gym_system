from flask import jsonify, request
from . import api_bp

@api_bp.route("/post", methods=["POST"])
def post():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username == "test" and password == "1234":
        return jsonify({"message": "Login successful", "token": "fake-jwt-token"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401