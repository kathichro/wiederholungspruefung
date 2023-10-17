from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user 
#from flask_wtf import FlaskForm
from flask_bcrypt import Bcrypt
#from wtforms import StringField, PasswordField, SubmitField
#from wtforms.validators import  InputRequired, Length, ValidationError
#from user import User
import forms


#from db import db, User, Todo, List, insert_sample  # (1.)

app = Flask(__name__)
#db = SQLAlchemy(app) warum zweite DB? Gibt´es schon bei db.py (Moath hat geregelt)
bcrypt = Bcrypt(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.sqlite' #kommt hier wirklich SQLite hin? Außerdem hab ich das auch bei db.py
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.py' #bei 11:50 guccken!!

#app.config['SECRET_KEY'] = 'secret_key_from_katharina_wiederholungspruefung'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    #from user import User
   return User.query.get(int(user_id))

app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment_Katharina_wiederholungspruefung',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)


bootstrap = Bootstrap5(app)

@app.route('/index')
@app.route('/')
def index():
    return redirect(url_for('todos')) #muss ich hier return render_template ('login.html') machen? ICH DENKE JA
                                        #so kommt es nämlich beim starten der seite zuerst zu login :)
                                        #muss mir halt überlegen was die startseite sein soll....
#überall einfügen "@login_required" ?? Weil soll man ja eig alles nur können wenn man eingeloggt ist 


@app.route('/login', methods=['GET', 'Post'])
def login():
    form =forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() #zum schauen, ob der User in der Datenbank existiert existiert
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('todos'))
    return render_template('login.html', form=form)

@app.route('/register',  methods=['GET', 'Post'])
def register():
    form = forms.RegisterForm()

    if request.method == 'POST':

        existing_user_username = User.query.filter_by(
           username=form.username.data).first()
        if not existing_user_username:
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user) #Das geht bestimmt nicht, weil ich kein datenbank.db hab...
            db.session.commit() # Das gilt für das denke ich auch mal....
            return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/logout',  methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/todos/', methods=['GET', 'POST'])
def todos():
    form = forms.CreateTodoForm()
    if request.method == 'GET':
        todos = db.session.execute(db.select(Todo).order_by(Todo.id)).scalars()  # !!
        return render_template('todos.html', todos=todos, form=form)
    else:  # request.method == 'POST'
        if form.validate():
            todo = Todo(description=form.description.data)  # !!
            db.session.add(todo)  # !!
            db.session.commit()  # !!
            flash('Todo has been created.', 'success')
        else:
            flash('No todo creation: validation error.', 'warning')
        return redirect(url_for('todos'))

@app.route('/todos/<int:id>', methods=['GET', 'POST'])
def todo(id):
    todo = db.session.get(Todo, id)  # !!
    form = forms.TodoForm(obj=todo)  # (2.)  # !!
    if request.method == 'GET':
        if todo:
            if todo.lists: form.list_id.data = todo.lists[0].id  # (3.)  # !!
            choices = db.session.execute(db.select(List).order_by(List.name)).scalars()  # !!
            form.list_id.choices = [(0, 'List?')] + [(c.id, c.name) for c in choices]  # !!
            return render_template('todo.html', form=form)
        else:
            abort(404)
    else:  # request.method == 'POST'
        if form.method.data == 'PATCH':
            if form.validate():
                form.populate_obj(todo)  # (4.)
                todo.populate_lists([form.list_id.data])  # (5.)  # !!
                db.session.add(todo)  # !!
                db.session.commit()  # !!
                flash('Todo has been updated.', 'success')
            else:
                flash('No todo update: validation error.', 'warning')
            return redirect(url_for('todo', id=id))
        elif form.method.data == 'DELETE':
            db.session.delete(todo)  # !!
            db.session.commit()  # !!
            flash('Todo has been deleted.', 'success')
            return redirect(url_for('todos'), 303)
        else:
            flash('Nothing happened.', 'info')
            return redirect(url_for('todo', id=id))

@app.route('/lists/')
def lists():
    lists = db.session.execute(db.select(List).order_by(List.name)).scalars()  # (6.)  # !!
    return render_template('lists.html', lists=lists)

@app.route('/lists/<int:id>')
def list(id):
    list = db.session.get(List, id)  # !!
    if list is not None:
        return render_template('list.html', list=list)
    else:
        return redirect(url_for('lists'))

@app.route('/insert/sample')
def run_insert_sample():
    insert_sample()
    return 'Database flushed and populated with some sample data.'

@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500

@app.get('/faq/<css>')
@app.get('/faq/', defaults={'css': 'default'})
def faq(css):
    return render_template('faq.html', css=css)

@app.get('/ex/<int:id>')
@app.get('/ex/', defaults={'id':1})
def ex(id):
    if id == 1:
        return render_template('ex1.html')
    elif id == 2:
        return render_template('ex2.html')
    else:
        abort(404)

from db import db, User, Todo, List, insert_sample  # (1.) wichtig hier