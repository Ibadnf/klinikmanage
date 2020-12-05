from flask import Blueprint, redirect, render_template, url_for, flash
from flask_login import LoginManager, login_user, current_user, login_required, logout_user, UserMixin
from app.extensions._db import db

main = Blueprint('main', __name__)
login_manager = LoginManager()

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/poliklinik')
@login_required
def poliklinik():
    return render_template('/poliklinik/poliklinik.html')

@main.route('/tambahpoliklinik')
@login_required
def create_poli():
    return render_template('/poliklinik/create_poli.html')

@main.route('/updatepoliklinik')
@login_required
def update_poli():
    return render_template('/poliklinik/update_poli.html')

@main.route('/deletepoliklinik')
@login_required
def delete_poli():
    return redirect(url_for('main.poliklinik'))

@main.route('/dokter')
@login_required
def dokter():
    return render_template('/dokter/dokter.html')