from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_cors import CORS

db = SQLAlchemy(session_options={'autocommit': False})


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    CORS(app)

    db.init_app(app)

    from .api_1_0 import api_text_label as api_text_label_blueprint
    app.register_blueprint(api_text_label_blueprint, url_prefix='/txtlabel')

    return app
