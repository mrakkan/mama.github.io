from . import db # from this package (. = website folder)
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # data = db.Column(db.String(10000), nullable-False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # user.id => class User



class User(db.Model, UserMixin):
    ###
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    # id & email = db.Column(db.String(150), unique=True) ใช้ไม่ได้ ต้องเขียน nullableด้วย

    password = db.Column(db.String(150))

    notes = db.relationship('Note') # => class Note
    ###