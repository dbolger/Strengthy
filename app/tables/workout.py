from app import db, login_manager
import enum


# Represents an individual exercise
class Exercise(db.Model):
    __tablename__ = "exercises"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sets = db.Column(db.Integer)
    units = db.Column(db.Integer)
    type = db.Column(db.Enum("reps", "time"), nullable=False)
    # Workout Relationship
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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # relationships
    exercises = db.relationship("Exercise", backref="workout", lazy="dynamic")

    def __init__(self, user, name, exercises):
        self.name = name
        self.user_id = user.id

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


# Connects workouts to it's exercises
# class WorkoutExercise(db.Model):
#    __table__ = 'workout_exercises'
#    id = db.Column(db.Integer, primary_key=True)
#    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
#    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
