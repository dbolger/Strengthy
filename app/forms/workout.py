from flask_wtf import FlaskForm, Form
from wtforms import FieldList, FormField, IntegerField, StringField
from wtforms.validators import DataRequired, Email

# Subclasses
class ExerciseCreateForm(Form):
    name = StringField("name",  [DataRequired()])
    sets = IntegerField("sets", [DataRequired()])
    units = IntegerField("units", [DataRequired()])

class SetForm(Form):
    lbs = IntegerField("lbs", [DataRequired()])
    reps = IntegerField("reps", [DataRequired()])

class ExerciseRecordForm(Form):
    sets = FieldList(FormField(SetForm))

# Actual forms
class WorkoutCreateForm(FlaskForm):
    name = StringField("name", [DataRequired()])
    exercises = FieldList(FormField(ExerciseCreateForm), min_entries=1)

class WorkoutRecordForm(FlaskForm):
    exercises = FieldList(FormField(ExerciseRecordForm))
