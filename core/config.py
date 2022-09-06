import os


class Config:
    APP_DEBUG = True
    # Database
    MYSQL_HOST = "localhost"
    MYSQL_PORT = "3306"
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "root"
    MYSQL_DATABASE = "scg_loyalty_hub"

    # JWT
    SECRET_KEY = "1bdob12ig80e1h29hed01h209d0912h"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
