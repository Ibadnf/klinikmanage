from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField, validators
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_wtf import FlaskForm, RecaptchaField
from app.models.users import UsersModel

class EditProfileForm(FlaskForm):
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
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm_password = PasswordField('Repeat Password', [
        validators.InputRequired(message='Confirm Password')
    ])
    submit_button = SubmitField('Submit')

    def validate_username(self, username):
        user = UsersModel.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = UsersModel.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
