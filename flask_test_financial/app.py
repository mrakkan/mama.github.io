from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime
# from views import views



#### from table.py ####
db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financial_test_datetime.db'
db.init_app(app)
#### ####


#### from models.py ####
class Task(db.Model):
    id = mapped_column(Integer, primary_key=True, nullable=False)
###
    datetime:Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    income: Mapped[float] = mapped_column(Float, nullable=False)
    outcome = mapped_column(Float)
    savings = mapped_column(Float)
    category = mapped_column(Float)
    
    sumincome = mapped_column(Float)
    sumoutcome = mapped_column(Float)
    sumsavings = mapped_column(Float)
    balance = mapped_column(Float)
### nullable = True or False wa




with app.app_context():
    db.create_all()
#### ####


@app.route('/finance/home', methods=['GET', 'POST'])
def finance_home():
    if request.method == 'POST':
        income = request.form.get('income')
        outcome = request.form['outcome']
        #
        savings = request.form['savings']
        category = request.form['category']

        # datetime = request.form
        print(income)
        print(outcome)

        myfinance = Task(income=income, outcome=outcome, savings=savings, category=category) #####

        db.session.add(myfinance)
        db.session.commit()


    return render_template('testinput.html')

@app.route('/finance/history')
def finance_history():
    return '<h>finance history</h>'






#### from run.py ####


if __name__ == '__main__':
    app.run(debug=True)
#### ####