from flask import Blueprint, render_template
from config import Config

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def posts_list():
    return render_template('posts_list.html', title='Блог', menu=Config.menu, brand=Config.brand)
