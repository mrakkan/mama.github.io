from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from os import path # ! ห้ามลบ


db = SQLAlchemy()
DB_NAME = 'database_finance_todolist3.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'we have to set secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # f-string
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .model import User, Todo, Finance


### ต้องใช้แบบนี้เท่านั้น น่าจะเพราะ sqlalchemy คนละ version
    with app.app_context():
        db.create_all()
###

#### * START flask_login ####
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
#### * END flask_login ####

### def create_database(app): & db.create_all(app=app) ใช้ไม่ได้ ทำไมไม่รู้(อีกละ)
### มันให้เอา parameter : app ออก
