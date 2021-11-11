from os import environ


class Config(object):
    """Base configuration."""

    DB_HOST = "bd_name"
    DB_USER = "db_user"
    DB_PASS = "db_pass"
    DB_NAME = "db_name"
    SECRET_KEY = "secret"

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass


class ProductionConfig(Config):
    """Production configuration."""

    DB_HOST = environ.get("DB_HOST", "ec2-3-229-166-245.compute-1.amazonaws.com")
    DB_USER = environ.get("DB_USER", "zpelobskvavivq")
    DB_PASS = environ.get("DB_PASS", "ce25c80e421910ecf6b50bc029334514ec803cf172360407b4bcd8e154a8c6f6")
    DB_NAME = environ.get("DB_NAME", "ddk8iuo2v4lcqv")
    DB_PORT = environ.get("DB_PORT", "5432")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        f"postgres://zpelobskvavivq:ce25c80e421910ecf6b50bc029334514ec803cf172360407b4bcd8e154a8c6f6@ec2-3-229-166-245.compute-1.amazonaws.com:5432/ddk8iuo2v4lcqv"
    )

class DevelopmentConfig(Config):
    """Development configuration."""

    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "MY_DB_USER")
    DB_PASS = environ.get("DB_PASS", "MY_DB_PASS")
    DB_NAME = environ.get("DB_NAME", "MY_DB_NAME")
    DB_PORT = environ.get("DB_PORT", "3306")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    # sqlalchemy no usa por defecto pymysql, agregando estas sentencias, yo le digo que se conecte a mi base de datos


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "MY_DB_USER")
    DB_PASS = environ.get("DB_PASS", "MY_DB_PASS")
    DB_NAME = environ.get("DB_NAME", "MY_DB_NAME")


config = dict(
    development=DevelopmentConfig, test=TestingConfig, production=ProductionConfig
)

# More information
# https://flask.palletsprojects.com/en/2.0.x/config/
