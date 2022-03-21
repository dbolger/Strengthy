from app import app
from database import database_get
from flask import render_template

@app.route("/", methods=["GET"])
def index():
    db = database_get()
    return render_template('base/index.html')
