from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Importar y registrar rutas
    from .app import main
    app.register_blueprint(main)

    return app
