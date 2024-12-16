from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_migrate import Migrate
import logging

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    
    migrate.init_app(app, db)

    # Import models to make them available to Flask-Migrate
    # from app.models import User

    # Register blueprints
    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    logging.basicConfig(level=logging.INFO)
    app.logger.info("Flask app starting up")

    return app