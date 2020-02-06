from flask import Flask, render_template, url_for
app = Flask(__name__)

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
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)