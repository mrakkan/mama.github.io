from . import db # from this package (. = website folder)
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Integer,  String, DateTime, Float, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from datetime import datetime, timedelta, timezone



class User(db.Model, UserMixin):
    id = mapped_column(Integer, primary_key=True, nullable=False)
    email = mapped_column(String(150), unique=True, nullable=False)
    password = mapped_column(String(150))
    notes = relationship('Note')
    finances = relationship('Finance')



class Note(db.Model):
    id = mapped_column(Integer, primary_key=True)
    data = mapped_column(String(10000))
    date = mapped_column(DateTime(timezone=True), default=func.now())
    user_id = mapped_column(Integer, ForeignKey('user.id'))



class Finance(db.Model):
    id = mapped_column(Integer, primary_key=True, nullable=False)
    user_id = mapped_column(Integer, ForeignKey('user.id'))

    datetime = mapped_column(DateTime(timezone=True), \
                                default=datetime.now(timezone(timedelta(hours=7))), nullable=False)
    income = mapped_column(Float)
    outcome = mapped_column(Float)
    savings = mapped_column(Float)
    category = mapped_column(String)

    sumincome = mapped_column(Float)
    sumoutcome = mapped_column(Float)
    sumsavings = mapped_column(Float)

    balance = mapped_column(Float)

    food = mapped_column(Float)
    education = mapped_column(Float)
    goodsservices = mapped_column(Float)
    travelfare = mapped_column(Float)
    other = mapped_column(Float)

    sum_food = mapped_column(Float)
    sum_education = mapped_column(Float)
    sum_goodsservices = mapped_column(Float)
    sum_travelfare = mapped_column(Float)
    sum_other = mapped_column(Float)

