from app import app
from flask import render_template
from config import Config


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Домашняя страничка', menu=Config.menu, brand=Config.brand)


@app.route('/about')
def about():
    return render_template('about.html', title='О сайте', menu=Config.menu, brand=Config.brand)