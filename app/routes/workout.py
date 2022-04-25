from app import app, db
from datetime import datetime
from flask import render_template, redirect, request, url_for, flash
from flask_login import current_user, login_required
from forms import WorkoutCreateForm, WorkoutRecordForm
from tables import Exercise, User, Workout, WorkoutRecord, SetRecord


@app.route("/workout/create", methods=["GET", "POST"])
@login_required
def workout_create():
    form = WorkoutCreateForm()
    name = form.name.data

    if form.validate_on_submit():
        # Make sure the user doesn't already have a workout with this name
        workout = Workout.query.filter_by(user_id=current_user.id, name=name).first()
        if not workout:
            # TODO: add exercises
            workout = Workout(
                current_user, name, [e.data for e in form.exercises.entries]
            )
            db.session.add(workout)
            db.session.commit()

            return redirect(url_for("home"))
        else:
            flash("Workout with this name already exists", "danger")
    else:
        print(form)
        print(form.errors)

    return render_template("workout/create.html", form=form)


@app.route("/workout/edit", methods=["GET", "POST"])
@login_required
def workout_edit():
    # Id is required
    if "id" not in request.args:
        return redirect(url_for("home"))

    # Validate Id
    workout = Workout.query.filter_by(
        id=int(request.args["id"]), user_id=current_user.id
    ).first()
    if not workout:
        return redirect(url_for("home"))

    form = WorkoutCreateForm()

    if form.validate_on_submit():
        # Form has been submitted, write changes FIXME
        for entry in form.exercises.entries:
            # Get the specified exercise TODO needs hidden id field
            exercise = Exercise.query.filter_by(
                workout_id=workout.id, id=int(entry.data["id"])
            ).first()

            if not exercise:
                continue

            # Update exercise
            exercise.name = entry.data["name"]
            exercise.sets = entry.data["sets"]
            exercise.units = entry.data["units"]
            exercise.type = entry.data["type"]

        # Write changes to database
        db.session.commit()
        return redirect(url_for("home"))
    else:
        form.name.data = workout.name
        form.exercises.pop_entry()  # TODO: better way to do this?

        for exercise in workout.exercises:
            form.exercises.append_entry(exercise)

    return render_template(
        "workout/create.html", form=form, title=f'Edit Workout "{workout.name}"'
    )


@app.route("/workout/record", methods=["GET", "POST"])
@login_required
def workout_record():
    form = WorkoutRecordForm()

    # Id is required
    if "id" not in request.args:
        return redirect(url_for("home"))

    # Matching workout required
    workout = Workout.query.filter_by(
        id=int(request.args["id"]), user_id=current_user.id
    ).first()
    if not workout:
        return redirect(url_for("home"))

    if form.validate_on_submit():
        # Form has been submitted and is valid
        workout_record = WorkoutRecord(workout, datetime.now())

        # Interate over form exercise entries
        for ee in form.exercises.entries:
            id = ee.data["id"]

            # And over that exercise's sets
            for se in ee.sets.entries:
                lbs = se.data["lbs"]
                units = se.data["units"]

                if lbs and units:
                    # Add the set to the workout record
                    workout_record.sets.append(
                        SetRecord(lbs=lbs, reps=units, exercise_id=id)
                    )

        db.session.add(workout_record)
        db.session.commit()

        return redirect(url_for("home"))
    else:
        # Populate form with data
        for exercise in workout.exercises:
            form.exercises.append_entry(
                {"id": exercise.id, "sets": [{}] * exercise.sets}
            )

        return render_template("workout/record.html", workout=workout, form=form)


@app.route("/workout/select", methods=["GET"])
@login_required
def workout_select():
    return render_template("workout/select.html")
