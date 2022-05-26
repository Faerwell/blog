from app import app
from flask import render_template
from config import Config


@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html', title='Blog Home Page', head_text='Главная страничка', menu=Config.menu,
                           brand=Config.brand)