import os
from flask import Flask
from .extensions import db
from .api.routes import api_dp
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
    app.register_blueprint(api_dp, url_prefix="/api")

    # execute_function(app)

    return app

def execute_function(app):
    with app.app_context():
        init_db()