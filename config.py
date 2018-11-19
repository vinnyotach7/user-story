import os


class Config:
    # MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringaschool:kalonje2018@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:kalonje2018@localhost/pitch'
    # pass


class DevConfig(Config):
    
    # pass
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production': ProdConfig,
    # 'test':TestConfig
}
