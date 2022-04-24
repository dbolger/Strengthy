from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Setup app before doing imports
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "super duper secret"  # FIXME: do not use in prod
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../strengthy.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Setup flask-login
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "/login"

# Setup SQLAlchemy
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
db = SQLAlchemy(app)
# TODO: do in script
import tables.user

db.create_all()

# Load routes
import routes
