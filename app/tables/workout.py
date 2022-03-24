from app import db, login_manager

# Represents an individual exercise
class Exercise(db.Model)
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)

# Represents a singular workout
class Workout(db.Model)
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Connects workouts to it's exercises
class WorkoutExercise(db.Model)
    __table__ = 'workout_exercises'
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
