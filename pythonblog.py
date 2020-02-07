from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'o3houx9pns4e1imzbv54'

posts = [
    {
        'author': 'Josh Benson',
        'title': 'Blog Post 1',
        'content': 'New content',
        'date_posted': 'Febuary 4, 2020'
    },
    {
        'author': 'Josh Smenson',
        'title': 'Blog Post 2',
        'content': 'Newer content',
        'date_posted': 'Febuary 5, 2020'
    },
    {
        'author': 'El Simon',
        'title': 'Blog Post 3',
        'content': 'Hot take: Pinapple on pizza is good. CENSOR*D.',
        'date_posted': 'Febuary 7, 2020'
    },
    {
        'author': 'Anonamous',
        'title': 'Blog Post 5',
        'content': 'Hot take: Self described centrists are not any better than conservatives',
        'date_posted': 'Febuary 7, 2020'
    },
    {
        'author': 'Pee pee poo poo',
        'title': 'Blog Post 6',
        'content': 'Hot take: I dont care about the news?',
        'date_posted': 'Febuary 7, 2020'
    },
    {
        'author': 'Pee pee poo poos twin sister',
        'title': 'Blog Post 7',
        'content': 'Hot take: Everytime Pr***k and ****ie leave they are hooking up',
        'date_posted': 'Febuary 7, 2020'
    },
    {
        'author': 'Protik',
        'title': 'Blog Post 8',
        'content': 'Hot take: Names without the letter "n" are better than names that contain the letter "n." Hobbes. Case in Point',
        'date_posted': 'Febuary 7, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Sign Up', form=form)

@app.route("/login")
def register():
    form = LoginForm()
    return render_template('login.html', title='Log In', form=form)


if __name__ == '__main__':
    app.run(debug=True)