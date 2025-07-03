from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'John Doe',
        'title': 'First Post',
        'content': 'This is the content of the first post.',
        'date_posted': 'April 20, 2023'
    },
    {
        'author': 'Jane Smith',
        'title': 'Second Post',
        'content': 'This is the content of the second post.',
        'date_posted': 'April 21, 2023'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About Page')

if( __name__ == '__main__'):
    app.run(debug=True)