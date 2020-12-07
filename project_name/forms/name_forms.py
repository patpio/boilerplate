from flask_wtf import FlaskForm
from wtforms import StringField


class NameForm(FlaskForm):
    name = StringField('Name')
