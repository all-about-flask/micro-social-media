from . import app
from flask import render_template


@app.route('/')
@app.route('/index')
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
