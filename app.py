from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Blog Home Page', head_text='Главная страничка')

@app.route('/about')
def about():
    return render_template('about.html', title='About Page', head_text='О сайте')

if __name__ == "__main__":
    app.run(debug=True)