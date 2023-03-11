from flask import Flask
from flask_restx import Api
from .utils import db
from .config.config import config_dict


def create_app(config=config_dict['dev']):
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)

    api = Api(app)

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
        }

    return app
