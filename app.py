from flask import Flask, render_template

from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

@app.route('/')
def home():
    return render_template ("index.html")


@app.route('/contact')
def contact():
    return render_template ("contact.html")


@app.route('/menu')
def menu():
    return render_template ("menu.html")


@app.route('/about')
def about():
    return render_template ("about.html")    


if __name__ == '__main__':
    app.debug = True 
    app.run()