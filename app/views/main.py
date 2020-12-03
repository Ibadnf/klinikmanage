from flask import Blueprint, redirect, render_template, url_for, flash
from flask_login import LoginManager, login_user, current_user, login_required, logout_user, UserMixin
from app.extensions._db import db

main = Blueprint('main', __name__)
login_manager = LoginManager()

@main.route('/dashboard')
def dashboard():
    if not current_user.is_authenticated:
    	    flash('Please login!', 'danger')
    	    return redirect(url_for('auth.login'))
    
    return render_template('dashboard.html')