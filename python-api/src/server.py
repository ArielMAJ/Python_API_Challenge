"""Server module."""

from flasgger import Swagger
from flask import Flask
from flask.blueprints import Blueprint
from flask_cors import CORS

import routes
from config import Config, DevelopmentConfig
from models import db


def create_app(config_name):
    """Creates the application and returns it to the user."""
    _server = Flask(__name__)

    _server.config["SWAGGER"] = {
        "swagger_version": "2.0",
        "title": "Application",
        "specs": [
            {
                "version": "0.0.1",
                "title": "Application",
                "endpoint": "spec",
                "route": "/application/spec",
                "rule_filter": lambda rule: True,  # all in
            }
        ],
        "static_url_path": "/apidocs",
    }

    Swagger(_server)

    _server.config.from_object(config_name)
    db.init_app(_server)
    db.app = _server

    for blueprint in vars(routes).values():
        if isinstance(blueprint, Blueprint):
            _server.register_blueprint(
                blueprint, url_prefix=Config.APPLICATION_ROOT
            )

    return _server


if __name__ == "__main__":
    server = create_app(DevelopmentConfig)
    with server.app_context():
        db.create_all()
    cors = CORS(server, resources={r"/*": {"origins": "*"}})

    print(f"Server running at http://{Config.HOST}:{Config.PORT}/")
    print(f"Swagger UI running at http://{Config.HOST}:{Config.PORT}/apidocs/")
    server.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
