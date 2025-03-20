from flask import jsonify, request
from . import api_bp
import re
from datetime import datetime
from models.user import User


def validate_user(data):
    try:
        name=data.get("name")
        phone=data.get("phone")
        gender=data.get("gender")
        height=data.get("height")
        weight=data.get("weight")

        # name (eq or less than 50)
        if not isinstance(name, str) or len(name) > 50:
            return "Invalid name"

        # phone (digit 10~13)
        if not re.match(r"^0\d{1,2}-\d{3,4}-\d{4}$", phone):
            return "Invalid phone number"

        # gender (male / female)
        if gender not in ["male", "female"]:
            return "Invalid gender (male or female expected)"

        # height
        if height is not None:
            try:
                height = float(height)
                if height <= 0 or height > 999:
                    return "Invalid height"
            except ValueError:
                return "Invalid height (must be a number)"

        # weight
        if weight is not None:
            try:
                weight = float(weight)
                if weight <= 0 or weight > 999:
                    return "Invalid weight"
            except ValueError:
                return "Invalid weight (must be a number)"

        return None
    except KeyError as e:
        return f"Missing field: {str(e)}"
    
# user register
@api_bp.route("/user_register", methods=["POST"])
def register():
    data = request.json

    error = validate_user(data)
    if error:
        return jsonify({"error": error}), 400

    # create user
    new_user = User(
        name=data.get("name"),
        phone=data.get("phone"),
        gender=data.get("gender"),
        height=data.get("height"),
        weight=data.get("weight"),
    )
    
    # TODO DB access
    
    return jsonify({"message": "User registered successfully", "user": new_user.to_dict()}), 201
