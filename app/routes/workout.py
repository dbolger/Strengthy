from app import app, db
from flask import render_template, redirect, request, url_for, flash
from flask_login import current_user, login_required
from forms import LoginForm, RegisterForm, WorkoutCreateForm
from tables import User, Workout

@app.route("/workout/create", methods=['GET', 'POST'])
@login_required
def createWorkout():
    form = WorkoutCreateForm()
    name = form.name.data

    if form.validate_on_submit():
        # Make sure the user doesn't already have a workout with this name
        workout = Workout.query.filter_by(user_id=current_user.id, name=name).first()
        if not workout:
            # TODO: add exercises
            workout = Workout(current_user, name, [e.data for e in form.exercises.entries])
            db.session.add(workout)
            db.session.commit()

            return redirect(url_for('home'));
        else:
            flash("Workout with this name already exists", "danger")

    return render_template('workout/create.html', form=form, title="Create a Workout")

@app.route("/workout/edit", methods=['GET', 'POST'])
@login_required
def editWorkout():
    # Id is required
    if 'id' not in request.args:
        return redirect(url_for('home'))

    # Validate Id
    workout = Workout.query.filter_by(id=int(request.args['id']), user_id=current_user.id).first()
    if not workout:
        return redirect(url_for('home'))

    form = WorkoutCreateForm()

    if form.validate_on_submit():
        # Form has been submitted, write changes

        workout.name = form.name.data
        # TODO: Add exercise changes

        # Write changes to database
        db.session.commit()
        return redirect(url_for('home'));
    else:
        form.name.data = workout.name
        form.exercises.pop_entry() # TODO: better way to do this?

        for exercise in workout.exercises:
            form.exercises.append_entry(exercise)

    return render_template('workout/create.html', form=form, title=f'Edit Workout "{workout.name}"')

@app.route("/workout/record", methods=['GET'])
@login_required
def recordWorkout():
    # Id is required
    if 'id' not in request.args:
        return redirect(url_for('home'))

    # Matching workout required
    workout = Workout.query.filter_by(id=int(request.args['id']), user_id=current_user.id).first()
    if not workout:
        return redirect(url_for('home'));

    return render_template('workout/record.html', workout=workout, form=None)

@app.route("/workout/select", methods=['GET'])
@login_required
def selectWorkout():
    return render_template('workout/select.html')
