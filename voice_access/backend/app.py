from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from mysql.connector import pooling
import os

from config import Config
# Blueprint import
from api import api_bp

# DB settings
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "test_db")

db_config = {
    "host":DB_HOST,
    "user":DB_USER,
    "password":DB_PASSWORD,
    "database":DB_NAME
}

user_api_pool = pooling.MySQLConnectionPool(
        pool_name="user_api_pool",
        pool_size=1,
        **db_config
)

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

jwt = JWTManager(app)

# blueprint register
app.register_blueprint(api_bp)

@app.route('/')
def home():
    return "Test page"

if __name__ == "__main__":
    app.run(debug=True, port=35000)