from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
db = SQLAlchemy(app)

# Import and register Blueprint
from app.routes import main
app.register_blueprint(main)
