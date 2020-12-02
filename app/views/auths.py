from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms.registers import RegisterForm
from app.forms.login import LoginForm
from app.models.users import UsersModel
from app.extensions._db import db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if request.method == 'POST':
        password = form.password.data
        hassed = generate_password_hash(password)

        user = UsersModel(
        username = request.form['username'],
        full_name = request.form['full_name'],
        email = request.form['email'],
        password = hassed
        )

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auths/register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    #allow user to login if no validation error
    if form.validate_on_submit():   
        user_object = UsersModel.query.filter_by(email=form.email.data).first()
        login_user(user_object)
        return redirect(url_for('index'))

    return render_template('auths/login.html', form=form)

@auth.route('/logout')
def logout():
    return redirect(url_for('index'))