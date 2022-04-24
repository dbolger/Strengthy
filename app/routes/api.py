from app import app, db
from flask import redirect, request
from flask_login import current_user, login_required
from tables import Workout


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
