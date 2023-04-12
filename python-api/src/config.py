"""
Configures the application and its environment.
"""
import logging
import os

from dotenv import load_dotenv

DIRNAME = os.path.join(os.path.dirname(__file__))

LOGGING_PATH = os.getenv(
    "SERVICE_LOG", os.path.join(DIRNAME, "logs", "server.log")
)
LOGS_DIR = os.path.dirname(LOGGING_PATH)
if not os.path.exists(LOGS_DIR):
    os.mkdir(LOGS_DIR)


class Config:
    """Base configuration."""

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    env_path = os.path.join(DIRNAME, "..", ".env")
    load_dotenv(env_path, verbose=True)

    DEBUG = os.getenv("ENVIRONEMENT") == "DEV"
    APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "")
    HOST = os.getenv("APPLICATION_HOST", "127.0.0.1")
    PORT = int(os.getenv("APPLICATION_PORT", "3000"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_CONTAINER = os.getenv("APPLICATION_DB_CONTAINER", "db")

    logging.basicConfig(
        filename=LOGGING_PATH,
        level=logging.DEBUG,
        format="%(levelname)s: %(asctime)s \
            pid:%(process)s module:%(module)s %(message)s",
        datefmt="%d/%m/%y %H:%M:%S",
    )


class DevelopmentConfig(Config):
    """Development configuration."""

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(DIRNAME, 'dev.db')}"


class ProductionConfig(Config):
    """Production configuration."""

    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{os.path.join(DIRNAME, 'production.db')}"
    )


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
