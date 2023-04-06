"""Server module."""

from flask import Flask
from flask.blueprints import Blueprint

import routes
from config import Config, DevelopmentConfig
from models import db


def create_app(config_name):
    """Creates the application and returns it to the user."""
    _server = Flask(__name__)

    _server.config.from_object(config_name)
    db.init_app(_server)
    db.app = _server

    for blueprint in vars(routes).values():
        if isinstance(blueprint, Blueprint):
            _server.register_blueprint(blueprint, url_prefix=Config.APPLICATION_ROOT)

    return _server


if __name__ == "__main__":
    server = create_app(DevelopmentConfig)
    with server.app_context():
        db.create_all()
    print(f"Server running at http://{Config.HOST}:{Config.PORT}/")
    server.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
