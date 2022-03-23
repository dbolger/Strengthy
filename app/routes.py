from app import app
from database import database_get
from flask import render_template
from login import *

@app.route("/", methods=["GET"])
def index():
    return render_template('base/index.html')

@app.route("/login", methods=["GET"])
def login():
    return render_template('user/login.html')

@app.route("/register", methods=["GET"])
def register():
    form = RegisterForm()

    #if form.validate_on_submit():
    #    # TODO: make sure username isnt taken somehow
    return render_template('user/register.html')
