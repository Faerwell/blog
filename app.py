from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
menu = [{'name': 'Главная', 'url': 'index'},
        {'name': 'О сайте', 'url': 'about'}]
brand = 'Faerwell'
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'


@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html', title='Blog Home Page', head_text='Главная страничка', menu=menu,
                           brand=brand)


@app.route('/about', methods=["POST", "GET"])
def about():
    if request.method == 'POST':
        print(request.form)
    if len(request.form['email']) != 0:
        flash('Сообщение отправлено', category='success')
    else:
        flash('Ошибка отправки', category='error')
    return render_template('about.html', title='About Page', head_text='О сайте', menu=menu, brand=brand)


@app.route('/profile/<username>')
def profile(username):
    return f'Пользователь: {username}'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('profile', username='Faerwell'))


if __name__ == "__main__":
    app.run(debug=True)