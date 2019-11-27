from flask_wtf import FlaskForm
from wtforms import SelectField

class UserForm(FlaskForm):
    state = SelectField('User', choices=[])
    city = SelectField('city', choices=[])
