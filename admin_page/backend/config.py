import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_secret_key")
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1H
    JWT_REFRESH_TOKEN_EXPIRES = 86400  # 1D