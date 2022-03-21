from flask import Flask

# Setup app before doing imports
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Load routes
import routes
