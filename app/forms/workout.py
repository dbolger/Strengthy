from flask_wtf import FlaskForm, Form
from wtforms import (
    FieldList,
    FormField,
    HiddenField,
    IntegerField,
    FloatField,
    SelectField,
    StringField,
)
from wtforms.validators import DataRequired, Email, Optional

# /workout/create
class ExerciseCreateForm(Form):
    id = HiddenField("id", [Optional()])
    name = StringField("name", [DataRequired()])
    sets = IntegerField("sets", [DataRequired()])
    units = FloatField("units", [DataRequired()])
    type = SelectField(
        "type", [DataRequired()], choices=[("reps", "Reps"), ("time", "Time")]
    )


class WorkoutCreateForm(FlaskForm):
    name = StringField("name", [DataRequired()])
    exercises = FieldList(FormField(ExerciseCreateForm), min_entries=1)


#  /workout/record
class SetForm(Form):
    lbs = FloatField("lbs", [Optional()])
    units = IntegerField("units", [Optional()])


class ExerciseRecordForm(Form):
    id = HiddenField("id", [DataRequired()])
    sets = FieldList(FormField(SetForm))


class WorkoutRecordForm(FlaskForm):
    exercises = FieldList(FormField(ExerciseRecordForm))
