import os
from flask import Flask, Blueprint
from .extensions import db
from .api.user_routes import user_dp
from .api.tag_routes import tag_dp
from config import config
from app.models import init_db

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV','default') or 'postgresql://postgres:root@localhost:5432/blogs'
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    #Initialisez les extensions
    db.init_app(app)



    #Enregistrez les bleueprints
    api_dp = Blueprint('api', __name__, url_prefix="/api")
    api_dp.register_blueprint(user_dp)
    api_dp.register_blueprint(tag_dp)

    app.register_blueprint(api_dp)

    #execute_function(app)

    return app

def execute_function(app):
    with app.app_context():
        init_db()