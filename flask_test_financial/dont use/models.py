from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from flask import Flask

from table import db


# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True, nullable=False)
#     date = db.Column(db.DateTime(timezone=True)) ###
#     salary = db.Column(db.Float)
#     balance = db.Column(db.Float)
#     savings = db.Column(db.Float)
#     spending = db.Column(db.Float)
#     category = db.Column(db.String) ###


class Task(db.Model):
    id:Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
###
    date:Mapped[int] = mapped_column(DateTime(timezone=True))
    salary:Mapped[int] = mapped_column(Float)
    balance:Mapped[int] = mapped_column(Float)
    savings:Mapped[int] = mapped_column(Float)
    spending:Mapped[int] = mapped_column(Float)
    category:Mapped[int] = mapped_column(String)
###