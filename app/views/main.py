from flask import Blueprint, redirect, render_template, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from app.extensions._db import db

main = Blueprint('main', __name__)
login_manager = LoginManager()