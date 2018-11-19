from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,forms,error
from flask_mail import Mail

mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    #........
    mail.init_app(app)