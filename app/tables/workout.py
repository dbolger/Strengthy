from app import db, login_manager
from flask_login import current_user
import enum


# Represents an individual exercise
class Exercise(db.Model):
    __tablename__ = "exercises"

    # fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sets = db.Column(db.Integer)
    units = db.Column(db.Integer)
    type = db.Column(db.Enum("reps", "time"), nullable=False)

    # foreign keys
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"))

    def __init__(self, name, sets, units, type):
        self.name = name
        self.sets = sets
        self.units = units
        self.type = type

    def __repr__(self):
        return f"<Exercise {self.name} {self.sets}x{self.units}>"


# Represents a singular workout
class Workout(db.Model):
    __tablename__ = "workouts"

    # fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # relationships
    exercises = db.relationship("Exercise", backref="workout", lazy="dynamic")
    records = db.relationship("WorkoutRecord", backref="workout", lazy="dynamic")

    def __init__(self, user, name, exercises):
        self.name = name
        self.user_id = user.id

        # populate exercises
        for exercise in exercises:
            self.exercises.append(
                Exercise(
                    exercise["name"],
                    exercise["sets"],
                    exercise["units"],
                    exercise["type"],
                )
            )

    def __repr__(self):
        return f"<Workout {self.name}>"


# Represents the recording of a single set within a workout recording
class SetRecord(db.Model):
    __tablename__ = "set_records"
    id = db.Column(db.Integer, primary_key=True)
    lbs = db.Column(db.Integer)
    reps = db.Column(db.Integer)

    # foreign keys
    workout_record_id = db.Column(db.Integer, db.ForeignKey("workout_records.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)

    # relationships
    exercise = db.relationship("Exercise")

    # Calculates using https://www.athlegan.com/calculate-1rm
    def one_rep_max(self):
        return int(self.lbs / (1.0278 - (0.0278 * self.reps)))


# Represents a recording of a workout
class WorkoutRecord(db.Model):
    __tablename__ = "workout_records"

    # fields
    id = db.Column(db.Integer, primary_key=True)
    finished = db.Column(db.DateTime)

    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"))

    # relationships
    sets = db.relationship("SetRecord", backref="workout_record", lazy="dynamic")

    def __init__(self, workout, finished):
        self.workout = workout
        self.finished = finished
        self.user = current_user

    def finished_nice(self, fmt="%m/%d/%y %-I:%M %p"):
        return self.finished.strftime(fmt)
