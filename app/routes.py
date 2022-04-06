from app import app, db
from flask import render_template, redirect, request, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from forms import LoginForm, RegisterForm, WorkoutCreateForm
from tables import User, Workout

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/home", methods=["GET"])
@login_required
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    username = form.username.data
    password = form.password.data

    if form.validate_on_submit():
        # Valid submission
        user = User.query.filter_by(username=username).first()

        # TODO: show user if login succeeded
        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password", "danger")

    return render_template('user/login.html', form=form)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect('/')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # Load data from form
    username = form.username.data
    password = form.password.data
    email = form.email.data

    if form.validate_on_submit():
        # Valid submission
        user = User.query.filter_by(username=username).first()
        if not user:
            # No user with this username
            user = User(username, password, email)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            flash("User already exists", "danger")

    return render_template('user/register.html', form=form)

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
