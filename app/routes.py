from . import app
from flask import render_template, flash, redirect
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Requested for user{}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/home')
    return render_template('login.html', title='Sign In', form=form)
