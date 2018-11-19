# import os


# class Config:
#     '''
#     General configuration parent class
#     '''
#     PITCH_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
#     PITCH_API_KEY = os.environ.get('PITCH_API_KEY')
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:kakabraza69@localhost/watchlist'
#     UPLOADED_PHOTOS_DEST = 'app/static/photos'
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


# class ProdConfig(Config):
#     '''
#     Production  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
#     pass


# class DevConfig(Config):
#     '''
#     Development  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2: // moringaschool: password@localhost/watchlist

#     DEBUG = True


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:password@localhost/watchlist_test'


# config_options = {
#     'development': DevConfig,
#     'production': ProdConfig,
#     'test': TestConfig
# }

# #  email configurations
# pass