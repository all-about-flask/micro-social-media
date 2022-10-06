from . import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/home')
def index():
    user = {'username': 'mdkovalesky'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Portland is Beautiful'
        },
        {
            'author': {'username': 'Sara'},
            'body': 'Disneyland is awesome'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)