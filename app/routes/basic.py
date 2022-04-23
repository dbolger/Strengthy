from app import app, db
from flask_login import login_required

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/home", methods=["GET"])
@login_required
def home():
    return render_template('home.html')
