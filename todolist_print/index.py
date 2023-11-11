from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
#postgres://mrakkan:zj5ghIylbzpiDDk2ykJcuJXH78JJKf6k@dpg-cl7qgkf6e7vc739vnp7g-a.singapore-postgres.render.com/mamadb

db.init_app(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/todo')
def todoshow():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()

    return render_template('todo.html', incomplete=incomplete, complete=complete)
@app.route('/main')
def home():
    return render_template('main.html')
@app.route('/add', methods=['POST'])
def add():
    todo_text = request.form['todoitem']
    if not todo_text:
        return redirect(url_for('todoshow'))
    todo = Todo(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('todoshow'))

@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    return redirect(url_for('todoshow'))
# def show():
#     completed = Todo.query.filter_by(complete=True).all()
#     incomplete = Todo.query.filter_by(complete=False).all()
#     db.session.commit()

#     print(len(completed), len(incomplete))
#     return {'completed': len(completed), 'incomplete': len(incomplete)}


if __name__ == '__main__':
    app.run(debug=True)
