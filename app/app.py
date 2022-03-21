from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('base/index.html')

@app.route("/login", methods=["GET"])
def login():
    return render_template('user/login.html')

@app.route("/register", methods=["GET"])
def register():
    return render_template('user/register.html')
