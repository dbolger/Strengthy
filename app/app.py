from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Setup app before doing imports
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = "super duper secret" # FIXME: do not use in prod
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://../strenghty.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setup SQLAlchemy
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
db = SQLAlchemy(app)

# Load routes
import routes
