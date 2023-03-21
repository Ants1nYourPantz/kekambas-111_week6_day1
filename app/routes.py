from app import app

from flask import render_template


@app.route('/')
def hello_world():
    return 'Hello World! Welcome to my blog.'



@app.route('/favorite_5')
def fav():
    return render_template('index.html')