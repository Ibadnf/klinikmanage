from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm, RecaptchaField
from app.models.users import UsersModel

class RegisterForm(FlaskForm):
    username = StringField('Username', [
        validators.InputRequired(message='Username Required')
        ])
    full_name = StringField('Full name', [
        validators.InputRequired(message='Full Name Required')
        ])
    email = StringField('Email', [
        validators.InputRequired(message='Email Required')
        ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.InputRequired(message='Password Required'),
        validators.EqualTo('confirm_password', message='Passwords must match')
    ])
    confirm_password = PasswordField('Repeat Password', [
        validators.InputRequired(message='Confirm Password')
    ])
    
    submit = SubmitField('Submit')
