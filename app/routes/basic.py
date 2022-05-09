from app import app, db
from flask import render_template
from flask_login import current_user, login_required
from tables import Workout, WorkoutRecord, SetRecord


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/home", methods=["GET"])
@login_required
def home():
    # Prepare so we don't have to do this in the template
    records = (
        db.session.query(WorkoutRecord)
        .filter_by(user_id=current_user.id)
        .order_by(WorkoutRecord.finished.desc())
    )

    sets_completed = (
        db.session.query(SetRecord, WorkoutRecord)
        .filter(
            WorkoutRecord.id == SetRecord.workout_record_id,
            WorkoutRecord.user_id == current_user.id,
        )
        .count()
    )

    return render_template("home.html", records=records, sets_completed=sets_completed)
