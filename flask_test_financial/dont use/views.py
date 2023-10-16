from flask import Flask, Blueprint, request, render_template, render_template_string
from flask_sqlalchemy import SQLAlchemy
from models import Task


db = SQLAlchemy()
views = Blueprint('views', __name__)


@views.route('/finance/home', methods=['GET', 'POST'])
def finance_home():
    if request.method == 'POST':
        salary = request.form.get('number')
        print(salary)

        salary = Task(salary=salary) #####

        
        db.session.add(salary)
        db.session.commit()

    #     message = 'yeah'

    #     return render_template('testinput.html', message=message)
    return render_template('testinput.html')

@views.route('finance/history')
def finance_history():
    return '<h>finance history</h>'
