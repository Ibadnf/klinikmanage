import os
from .default import Config

# setting for development staging
class Development(Config):
    DEBUG=True
    ENV='development'
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
