from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import views

db = SQLAlchemy()

def run():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financial_test.db'
    db.init_app(app)

    ### from .views import views ด้วย


    # class Task(db.Model):
    #     id = db.Column(db.Integer, primary_key=True, nullable=False)
    #     date = db.Column(db.DateTime(timezone=True)) ###
    #     salary = db.Column(db.Float)
    #     balance = db.Column(db.Float)
    #     savings = db.Column(db.Float)
    #     spending = db.Column(db.Float)
    #     category = db.Column(db.String) ###
    from models import Task


    app.register_blueprint(views, url_prefix='/')



    with app.app_context():
        db.create_all()


    return app




