from app import db, login_manager

# Represents an individual exercise
class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)

# Represents a singular workout
class Workout(db.Model):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # User Relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, user, name, exercises):
        self.name = name
        self.user_id = user.id

    def __repr__(self):
        return f'<Workout {self.name}>'

# Connects workouts to it's exercises
#class WorkoutExercise(db.Model):
#    __table__ = 'workout_exercises'
#    id = db.Column(db.Integer, primary_key=True)
#    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
#    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
