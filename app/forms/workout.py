from flask_wtf import FlaskForm, Form
from wtforms import (
    FieldList,
    FormField,
    HiddenField,
    IntegerField,
    SelectField,
    StringField,
)
from wtforms.validators import DataRequired, Email, Optional

# /workout/create
class ExerciseCreateForm(Form):
    # TODO no exercise_*, breaks workout_edit endpoint
    id = HiddenField("id", [DataRequired()])
    name = StringField("name", [DataRequired()])
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
    lbs = IntegerField("lbs", [Optional()])
    units = IntegerField("units", [Optional()])


class ExerciseRecordForm(Form):
    id = HiddenField("id", [DataRequired()])
    sets = FieldList(FormField(SetForm))


class WorkoutRecordForm(FlaskForm):
    exercises = FieldList(FormField(ExerciseRecordForm))
