from flask_wtf import FlaskForm, Form
from wtforms import FieldList, FormField, IntegerField, StringField
from wtforms.validators import DataRequired, Email

# Subclass, not used directly
class ExerciseForm(Form):
    name = StringField("name",  [DataRequired()])
    sets = IntegerField("sets", [DataRequired()])
    reps = IntegerField("reps", [DataRequired()])

class WorkoutCreateForm(FlaskForm):
    name = StringField("name", [DataRequired()])
    exercises = FieldList(FormField(ExerciseForm), min_entries=1)
