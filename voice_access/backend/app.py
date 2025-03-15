from flask import Flask
from mysql.connector import pooling
import os

# Blueprint import
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

# app.register_blueprint(home_bp)
# app.register_blueprint(db_bp, url_prefix='/db')

@app.route('/')
def home():
    return "Test page"

if __name__ == "__main__":
    app.run(debug=True, port=8080)