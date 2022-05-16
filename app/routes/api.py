from app import app, db
from flask import redirect, request, jsonify, url_for
from flask_login import current_user, login_required
from tables import Exercise, SetRecord, Workout, WorkoutRecord


@app.route("/api/workout/delete", methods=["GET"])
@login_required
def api_workout_delete():
    if "id" not in request.args:
        return redirect("/home")

    workout = Workout.query.filter_by(
        id=int(request.args["id"]), user_id=current_user.id
    ).first()
    if workout:
        db.session.delete(workout)
        db.session.commit()

    return redirect("/home")


@app.route("/api/progress/exercise/<exercise_id>", methods=["GET"])
@login_required
def api_progress_exercise(exercise_id=None):
    # Get exercise from database NOTE: consider adding userid to exercise
    exercise = (
        db.session.query(Exercise)
        .filter_by(id=exercise_id)
        .join(Workout, Workout.user_id == current_user.id)
        .first()
    )
    if not exercise:
        return redirect(url_for("home"))

    results = (
        db.session.query(WorkoutRecord.finished, db.func.max(SetRecord.lbs))
        # .join(SetRecord.workout_record_id == WorkoutRecord.id)
        .filter(
            SetRecord.exercise_id == exercise_id,
            WorkoutRecord.user_id == current_user.id,
            SetRecord.workout_record_id == WorkoutRecord.id,
        )
        .group_by(WorkoutRecord.id)
        .order_by(WorkoutRecord.finished)
    ).all()

    # prepare values TODO include date
    # jsonify can't handle objects so we have to do this hack
    values = [(row[0].strftime("%m/%d/%y"), row[1]) for row in results]

    response = jsonify(values)
    response.headers.add("Access-Control-Allow-Origin", "*")  # for AJAX
    return response
