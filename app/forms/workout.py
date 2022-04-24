from flask_wtf import FlaskForm, Form
from wtforms import FieldList, FormField, IntegerField, SelectField, StringField
from wtforms.validators import DataRequired, Email

# /workout/create
class ExerciseCreateForm(Form):
    # TODO no exercise_*, breaks workout_edit endpoint
    name = StringField("name", [DataRequired()], name="name")
    sets = IntegerField("sets", [DataRequired()])
    units = IntegerField("units", [DataRequired()])
    type = SelectField(
        "type", [DataRequired()], choices=[("reps", "Reps"), ("time", "Time")]
    )


class WorkoutCreateForm(FlaskForm):
    name = StringField("name", [DataRequired()])
    exercises = FieldList(FormField(ExerciseCreateForm), min_entries=1)


#  /workout/record
class SetForm(Form):
    lbs = IntegerField("lbs", [DataRequired()])
    reps = IntegerField("reps", [DataRequired()])


class ExerciseRecordForm(Form):
    sets = FieldList(FormField(SetForm))


# Actual forms
class WorkoutRecordForm(FlaskForm):
    exercises = FieldList(FormField(ExerciseRecordForm))
