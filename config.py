import os

class Config:
    """ Classe de configuration de base pour l'application """
    SECRET_KEY = os.environ.get("SECRET_KEY") or ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configuration pour l'environnement de développement."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost:5432/db_name_dev'

class ProductionConfig(Config):
    """Configuration pour l'environnement de production."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost:5432/db_name_prod'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}