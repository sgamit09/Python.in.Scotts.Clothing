from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "scotts_closet.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='POOPOOPEEPEEFARTBUTTHOLE'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Clothes

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader #decorator
    def load_user(id):
        return User.query.get(int(id))

    with app.app_context():
        db.create_all()

    return app

