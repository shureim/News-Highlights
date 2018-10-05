from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

Bootstrap = Bootstrap()

def create_app(config_name) :

    app = Flask(__name__)


    #creaticng  app configuration
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    Bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .requests import configure_request
    configure_request(app)

    return app



    
