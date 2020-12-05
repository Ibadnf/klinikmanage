from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, current_user, login_required, logout_user, UserMixin

from app.forms.registers import RegisterForm
from app.forms.login import LoginForm
from app.forms.edit import EditProfileForm
from app.models.users import UsersModel
from app.extensions._db import db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=('GET', 'POST'))
def register():

    form = RegisterForm()
    if request.method == 'POST':

        user = UsersModel(username=form.username.data, full_name=form.full_name.data, email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('auth.login'))

    return render_template('/auths/register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = LoginForm()

    #allow user to login if no validation error
    if form.validate_on_submit():
        user = UsersModel.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('main.dashboard'))

    return render_template('/auths/login.html', form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditProfileForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.full_name = form.full_name.data
        current_user.email = form.email.data
        current_user.password = form.password.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.full_name.data = current_user.full_name
        form.email.data = current_user.email
        form.password.data = current_user.password
    return render_template('/auths/edit_profile.html', form=form)