from . import db
from .model import User
from flask import Blueprint, render_template, request, flash, redirect, url_for

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

# from flask_login import *


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user_email_check = User.query.filter_by(email=email).first()

        if user_email_check:
            if check_password_hash(user_email_check.password, password):
                flash('Logged in successfully.', category='success')

                login_user(user_email_check, remember=True) # remember=False ก็คือไม่ต้องจำก็ได้
                # login_user(user_email_check, remember=False)

                return redirect(url_for('views.home')) # flask 3 redirect() เหมือนจะไม่มี (,response)
            else:
                flash('Incorrect password, please try again.', category='error')
        else:
            flash('Email doesn\'t exist.', category='error')

    return render_template('login.html')


## ! ตอนนี้ยังไม่มีให้กด log out ##
@auth.route('/logout')
@login_required
def logout():

    logout_user()
    return redirect(url_for('auth.login'))
## ! ##




@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
    # request.form => รับ data เข้ามาธรรมดา
        email = request.form.get('email')
        password = request.form.get('password')

        user_email_check = User.query.filter_by(email=email).first()

        if user_email_check:
            flash('Email already exist.', category='error')
        elif len(email) < 4:
            flash('Please enter your email', category='error')

        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')

        else:
            new_user = User(email=email, password=generate_password_hash(password, method='sha256'))
            # new_user = User(email=email, password=password) => โดนบังคับ hash ตรง check_password_hash()


            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True) # remember=False ไม่ต้องจำก็ได้
            # login_user(user_email_check, remember=False)

            flash('Account created', category='success')
            return redirect(url_for('auth.login'))
            # url_for('ชื่อไฟล์.function')


    return render_template('signup.html')


