import os

from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user, UserMixin

from app.models.users import UsersModel

def create_app():
    app = Flask(__name__)

    login = LoginManager(app)
    login.init_app(app)
    
    @login.user_loader
    def get_user(ident):
        return UsersModel.query.get(int(ident))

    # config
    app.config.from_object(os.environ['APP_CONFIG_FILE'])

    # extension
    from .extensions._db import db, setup_db
    setup_db(app)

    # view
    from app.views.auths import auth as auth
    app.register_blueprint(auth)

    from app.views.main import main as main
    app.register_blueprint(main)

    @app.route('/', methods=['GET'])
    def index():
        if not current_user.is_authenticated:
    	    flash('Please login!', 'danger')
    	    return redirect(url_for('auth.login'))

    return app