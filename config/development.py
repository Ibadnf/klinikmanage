from .default import Config

# setting for development staging
class Development(Config):
    DEBUG=True
    ENV='development'
    SQLALCHEMY_DATABASE_URI = 'postgresql://klinikmanage:ibadnf06@localhost/klinikmanage'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
