from app import app, db
from flask import render_template
from flask_login import current_user, login_required
from tables import Workout, WorkoutRecord


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/home", methods=["GET"])
@login_required
def home():
    # Prepare so we don't have to do this in the template
    records = (
        db.session.query(WorkoutRecord)
        .join(Workout)
        .filter(Workout.user_id == current_user.id)
    )

    return render_template("home.html", records=records)
