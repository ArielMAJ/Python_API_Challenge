"""Server module."""

from flask import Flask
from flask.blueprints import Blueprint

import config
import routes
from models import db

server = Flask(__name__)

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(server)
db.app = server

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

if __name__ == "__main__":
    with server.app_context():
        db.create_all()
    print(f"Server running at http://{config.HOST}:{config.PORT}/")
    server.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
