from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .model import Finance, Todo
from . import db


views = Blueprint('views', __name__)

@views.route('/')
def mama():
    return render_template('mama.html')


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    alltasklist = Finance.query.filter_by(user_id=current_user.id).all()
    history10 = alltasklist[11::-1]

    return render_template('home.html', history10=history10)



#### ? START main โชว์ขึ้นหน้าแรก ####
@views.route('/todo/smth')
@login_required
def main():
    financelist = Finance.query.filter_by(user_id=current_user.id).all()
    balance = 0
    if len(financelist) != 0:
        balance = (financelist[-1]).balance
    incomplete = Todo.query.filter_by(user_id=current_user.id, complete=False).all() # *
    username = current_user.email
    print(username)
    atcount = username.find('@')
    username = username[:atcount]

    return render_template('main.html', balance=balance, incomplete=incomplete, username=username)
#### ? END main ####



#?####################
#### ? START todo ####
@views.route('/todo')
@login_required
def todoshow():
    incomplete = Todo.query.filter_by(user_id=current_user.id, complete=False).all() # *
    complete = Todo.query.filter_by(user_id=current_user.id, complete=True).all() # *

    return render_template('todo.html', incomplete=incomplete, complete=complete) # *



@views.route('/todo/add', methods=['POST'])
@login_required
def add(): ## & add
    todo = request.form['todoitem']
    if not todo:
        return redirect(url_for('views.todoshow'))
    else:
        todo = Todo(user_id=current_user.id, text=todo, complete=False)
        db.session.add(todo)
        db.session.commit()

    return redirect(url_for('views.todoshow'))


@views.route('/todo/complete/<id>')
@login_required
def complete(id):
    todo = Todo.query.filter_by(id=int(id), user_id=current_user.id).first()
    if todo:
        todo.complete = True
        db.session.commit()
    return redirect(url_for('views.todoshow'))
#### ? END todo ####
#?####################



#?####################
#### ? START finance ####
@views.route('/fine', methods=['GET', 'POST'])
@login_required
def finnie():
    message = ''
    alltasklist = Finance.query.filter_by(user_id=current_user.id).all()
    history10 = alltasklist[11::-1]

    if len(alltasklist) == 0:
        sumincome = 0
        sumoutcome = 0
        sumsavings = 0
        balance = 0
        sum_food = 0
        sum_education = 0
        sum_goodsservices = 0
        sum_travelfare = 0
        sum_other = 0

    else:
        financelist = (Finance.query.filter_by(user_id=current_user.id).all())[-1]
        sumincome = (financelist).sumincome
        sumoutcome = (financelist).sumoutcome
        sumsavings = (financelist).sumsavings
        balance = (financelist).balance
        sum_food = (financelist).sum_food
        sum_education = (financelist).sum_education
        sum_goodsservices = (financelist).sum_goodsservices
        sum_travelfare = (financelist).sum_travelfare
        sum_other = (financelist).sum_other

    if request.method == 'POST':
        income = request.form['income']
        outcome = request.form['outcome']
        savings = request.form['savings']
        category = request.form['categories']

        if income == None or income == '':
             income = 0
        if outcome == None or outcome == '':
            outcome = 0
        if savings == None or savings == '':
            savings = 0
        if category == None or category == '':
            category = None

        alltask = Finance.query.filter_by(user_id=current_user.id)
        print(alltask)


        sumincome = sum([i.income for i in alltask]) + float(income)
        print('sumincome : ', sumincome)

        sumoutcome = sum([i.outcome for i in alltask]) + float(outcome)
        print('sumoutcome : ', sumoutcome)

        sumsavings = sum([i.savings for i in alltask]) + float(savings)
        print('sumsavings :', sumsavings)


        balance = sumincome - sumoutcome - sumsavings
        print('balance : ', balance)

        #### ? ####
        if balance < 0:
            message = 'ลูกแม่ เป็นหนี้เป็นสินแล้วลูก'
            sumincome -= float(income)
            sumoutcome -= float(outcome)
            sumsavings -= float(savings)

        else:
            if balance == 0:
                message = 'คนดีของแม่ เมิดดากละลูก'
        #### ? ####

            food = 0
            education = 0
            goodsservices = 0
            travelfare = 0
            other = 0

            if category == 'Food':
                food = outcome
            elif category == 'Education':
                education = outcome
            elif category == 'Goods & Services':
                goodsservices = outcome
            elif category == 'Fare':
                travelfare = outcome
            elif category == 'Other':
                other = outcome

            sum_food = sum([i.food for i in alltask]) + float(food)
            sum_education = sum([i.education for i in alltask]) + float(education)
            sum_goodsservices = sum([i.goodsservices for i in alltask]) + float(goodsservices)
            sum_travelfare = sum([i.travelfare for i in alltask]) + float(travelfare)
            sum_other = sum([i.other for i in alltask]) + float(other)
    
            finance(income, outcome ,savings, category, balance, \
            sumincome, sumoutcome, sumsavings, \
            food, education, goodsservices, travelfare, other,\
            sum_food, sum_education, sum_goodsservices, sum_travelfare, sum_other)

            alltasklist = Finance.query.filter_by(user_id=current_user.id).all()
            history10 = alltasklist[11::-1]

    return render_template('finance.html',sum_food=sum_food, sum_education=sum_education, sum_travelfare=sum_travelfare, \
                            sum_goodsservices=sum_goodsservices, sum_other=sum_other,
                            sumincome=sumincome, sumoutcome=sumoutcome, sumsavings=sumsavings, \
                            message=message, balance=balance, history10=history10)




@views.route('/finance', methods=['POST'])
@login_required
def finance(income, outcome ,savings, category, balance, \
            sumincome, sumoutcome, sumsavings, \
            food, education, goodsservices, travelfare, other,\
            sum_food, sum_education, sum_goodsservices, sum_travelfare, sum_other):

    if request.method == 'POST':

            myfinance = Finance(user_id=current_user.id ,income=income, outcome=outcome, savings=savings, \
                            category=category, balance=balance, \
                            sumincome=sumincome, sumoutcome=sumoutcome, sumsavings=sumsavings, \
                            food= food, education=education, goodsservices=goodsservices, travelfare=travelfare, other=other,\
                            sum_food=sum_food, sum_education=sum_education, sum_goodsservices=sum_goodsservices, \
                            sum_travelfare=sum_travelfare, sum_other=sum_other)

            db.session.add(myfinance)
            db.session.commit()

    return redirect(url_for('views.home'))

#### ? END finance ####
#?####################
