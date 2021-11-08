import os


class Config(object):
    """ Application config options """

    APPNAME = "gringotts"
    VERSION = "1.0.0"

    def __init__(self):
        self.SECRET_KEY = "gringotts-string-secret"


class DevelopmentConfig(Config):
    """ Dev environment config options """

    def __init__(self):
        super().__init__()

        self.FLASK_ENV = "development"
        self.DEBUG = True
        self.CRYPTO_KEY = os.environ.get("CRYPTO_KEY").encode()
        self.PASSWORD_FILE = os.environ.get("PASSWORD_FILE", "passwords.json")


class ProductionConfig(Config):
    """ Dev environment config options """

    def __init__(self):
        super().__init__()

        self.FLASK_ENV = "production"
        self.DEBUG = False
        self.CRYPTO_KEY = os.environ.get("CRYPTO_KEY").encode()
        self.PASSWORD_FILE = os.environ.get("PASSWORD_FILE", "passwords.json")


APP_CONFIG = {"development": DevelopmentConfig, "production": ProductionConfig}
