from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField, validators, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length, Optional
from werkzeug.security import check_password_hash
from app.models.users import UsersModel

def invalid_credentials(form, field):
    email_entered = form.email.data
    password_entered = field.data

    user = UsersModel.query.filter_by(email=form.email.data).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

class LoginForm(FlaskForm):
    email = StringField('Email', [
        validators.InputRequired(message='Email Required')
        ])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
