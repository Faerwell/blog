import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))


class Config:
    DEBUG = True
    menu = [{'name': 'Блог', 'url': 'posts.posts_list'},
            {'name': 'О сайте', 'url': 'about'}]
    brand = 'Faerwell'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATION = False