from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Daniel'}
    posts = [
        {
            'author': {'username': 'Liam'},
            'body': 'Good day today!'
        },
        {
            'author': {'username': 'Andrew'},
            'body': 'Last Jedi was a bad movie!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)