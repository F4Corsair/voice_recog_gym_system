from flask import Blueprint

api_bp = Blueprint("api", __name__, url_prefix="/api")

# from . import auth, get, post
from . import user_register, voice_auth, voice_register