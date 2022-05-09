from app import app, db
from flask import render_template
from flask_login import current_user, login_required
from tables import Workout, Exercise, WorkoutRecord, SetRecord


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/home", methods=["GET"])
@login_required
def home():
    # Workout records
    records = (
        db.session.query(WorkoutRecord)
        .filter_by(user_id=current_user.id)
        .order_by(WorkoutRecord.finished.desc())
        .all()
    )

    # Set records length
    sets_completed = (
        db.session.query(SetRecord, WorkoutRecord)
        .filter(
            WorkoutRecord.id == SetRecord.workout_record_id,
            WorkoutRecord.user_id == current_user.id,
        )
        .count()
    )

    # Top 3 exercises (by frequency)
    top3 = (
        db.session.query(Exercise)
        .join(SetRecord)
        .filter(SetRecord.exercise_id == Exercise.id)
        .group_by(Exercise.id)
        .order_by(db.func.count(SetRecord.id).desc())
        .having(db.func.count(SetRecord.id) > 1)
        .limit(3)
        .all()
    )

    return render_template(
        "home.html", records=records, sets_completed=sets_completed, top3=top3
    )
