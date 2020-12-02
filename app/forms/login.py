from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, EqualTo, Length, Optional
from app.models.users import UsersModel

class LoginForm(FlaskForm):
    email = StringField('Email', [
        validators.InputRequired(message='Email Required')
        ])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
