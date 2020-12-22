from flask_wtf import FlaskForm
from wtforms import StringField

class SampleForm(FlaskForm):
    name = StringField('Name')