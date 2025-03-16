from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from . import api_bp
import re
from datetime import datetime
from models.user import User

# test - TODO replace DB
users = {"test": "1234"}

def validate_user(data):
    try:
        name = data["name"]
        phone = data["phone"]
        birthdate = data["birthdate"]
        gender = data["gender"]
        height = data.get("height")
        weight = data.get("weight")

        # name (eq or less than 50)
        if not isinstance(name, str) or len(name) > 50:
            return "Invalid name"

        # phone (digit 10~15)
        if not re.match(r"^\d{10,15}$", phone):
            return "Invalid phone number"

        # birthday (YYYY-MM-DD)
        try:
            datetime.strptime(birthdate, "%Y-%m-%d")
        except ValueError:
            return "Invalid birthdate format (YYYY-MM-DD expected)"

        # gender (male / female)
        if gender not in ["male", "female"]:
            return "Invalid gender (male or female expected)"

        # height
        if height is not None:
            try:
                height = float(height)
                if weight <= 0:
                    return "Invalid height"
            except ValueError:
                return "Invalid height (must be a number)"

        # weight
        if weight is not None:
            try:
                weight = float(weight)
                if weight <= 0:
                    return "Invalid weight"
            except ValueError:
                return "Invalid weight (must be a number)"

        return None
    except KeyError as e:
        return f"Missing field: {str(e)}"
    

@api_bp.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # TODO user auth from DB
    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        return jsonify({"access_token": access_token, "refresh_token": refresh_token})
    
    return jsonify({"message": "Invalid credentials"}), 401

@api_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    new_access_token = create_access_token(identity=identity)
    return jsonify({"access_token": new_access_token})

# protected data access
@api_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": current_user})

# user register
@api_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    error = validate_user(data)
    if error:
        return jsonify({"error": error}), 400

    # create user
    new_user = User(
        name=data["name"],
        phone=data["phone"],
        birthdate=data["birthdate"],
        gender=data["gender"],
        height=data.get("height"),
        weight=data.get("weight"),
    )
    
    # TODO DB access
    users.append(new_user)
    
    return jsonify({"message": "User registered successfully", "user": new_user.to_dict()}), 201

@api_bp.route("/users", methods=["GET"])
def get_users():
    # TODO DB access
    return jsonify([user.to_dict() for user in users])