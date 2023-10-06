from flask import Blueprint, render_template, request
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
def mama():

    return render_template('mama.html')

@views.route('/home')
@login_required
def home():
    return '<h>home</h>' 
