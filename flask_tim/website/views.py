from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .model import Finance
from . import db


views = Blueprint('views', __name__)

@views.route('/')
def mama():

    return render_template('mama.html')

@views.route('/home')
@login_required
def home():
    return render_template('home.html')


@views.route('/home/finance', methods=['GET', 'POST'])
@login_required
def finance():
    if request.method == 'POST':
        income = request.form['income']
        outcome = request.form['outcome']
        savings = request.form['savings']
        category = request.form['category']

        print('income : ', income)
        print('outcome : ', outcome)
        print('savings : ', savings)
        print('category : ', category)

        if income == None or income == '':
             income = 0
        if outcome == None or outcome == '':
            outcome = 0
        if savings == None or savings == '':
            savings = 0
        if category == None or category == '':
            category = None

        print('-----after if else-----')
        print('income : ', income)
        print('outcome : ', outcome)
        print('savings : ', savings)
        print('category : ', category)


        alltasklist = Finance.query.filter_by(user_id=current_user.id)


        sumincome = sum([i.income for i in alltasklist]) + float(income)
        print('sumincome : ', sumincome)

        sumoutcome = sum([i.outcome for i in alltasklist]) + float(outcome)
        print('sumoutcome : ', sumoutcome)

        sumsavings = sum([i.savings for i in alltasklist]) + float(savings)
        print('sumsavings :', sumsavings)


        balance = sumincome - sumoutcome - sumsavings
        print('balance : ', balance)


        food = 0
        education = 0
        goodsservices = 0
        travelfare = 0
        other = 0

        if category == 'food':
            food = outcome
        elif category == 'education':
            education = outcome
        elif category == 'goodsservices':
            goodsservices = outcome
        elif category == 'travelfare':
            travelfare = outcome
        elif category == 'other':
            other = outcome

        sum_food = sum([i.food for i in alltasklist]) + float(food)
        sum_education = sum([i.education for i in alltasklist]) + float(education)
        sum_goodsservices = sum([i.goodsservices for i in alltasklist]) + float(goodsservices)
        sum_travelfare = sum([i.travelfare for i in alltasklist]) + float(travelfare)
        sum_other = sum([i.other for i in alltasklist]) + float(other)



        myfinance = Finance(user_id=current_user.id ,income=income, outcome=outcome, savings=savings, \
                        category=category, balance=balance, \
                        sumincome=sumincome, sumoutcome=sumoutcome, sumsavings=sumsavings, \
                        food= food, education=education, goodsservices=goodsservices, travelfare=travelfare, other=other,\
                        sum_food=sum_food, sum_education=sum_education, sum_goodsservices=sum_goodsservices, \
                        sum_travelfare=sum_travelfare, sum_other=sum_other)

        db.session.add(myfinance)
        db.session.commit()


    return render_template('testinput.html')
