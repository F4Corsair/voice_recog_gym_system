from flask import Flask
from flask_cors import CORS
from flask import Blueprint
from mysql.connector import pooling
import os

# Blueprint import
from api import api_bp
# from routes.home import home_bp
# from routes.db import db_bp

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

connection_pool = pooling.MySQLConnectionPool(
        pool_name="mypool",
        pool_size=20,
        **db_config
)

app = Flask(__name__)
CORS(app)

app.register_blueprint(api_bp)

@app.route('/')
def home():
    return "Test page"

if __name__ == "__main__":
    app.run(debug=True, port=8080)