from flaskBlogs import app, db
from flaskBlogs.forms import RegistrationForm, LoginForm
from flask import render_template, redirect, url_for, flash, request
from flaskBlogs.models import User, Post, Comment

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

@app.route('/post')
def post():
    return render_template('post.html', title='Post Page', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Here you would typically check the user's credentials and data and the home will be replaced with users data.
            # For now, we just redirect to the home page
            return redirect(url_for('home'))
    return render_template('login.html', title='Login Page', form=form, hide_sidebar=True)

@app.route('/register', methods=['GET', 'POST'])
def register():

    # @@@@@@@@@@@@@@@@@@@@----------Concepts on Flask-WTF Forms------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #Registration Form is an instance of Flask Form Class it automatically handles the CSRF token and form validation
    #It automatically populates the form fields with the data submitted by the user even it looks like you are doing a fresh instantiation of the form
    #
    #--------- Check this out --------->  form = RegistrationForm(request.form if request.method == 'POST' else None) 
    #
    # This is because Flask-WTF handles the form data and CSRF(check {{ form.hidden_tag() }} in the register.html and login.html it contains the CSRF token for security purposes) token automatically.
    #So, you don't need to pass the form data explicitly to the template.
    #The form data is automatically available in the form object.

    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():

            db.session.add(User(username=form.username.data, email=form.email.data, password=form.password.data))
            db.session.commit()

            flash('Registration successful for: ' + form.username.data, category='success') 
            # Here you would typically save the user's information to the database
            # For now, we just redirect to the home page
            print("Registration successful for:", form.username.data)
            return redirect(url_for('login'))
    return render_template('register.html', title='Register Page', form=form, hide_sidebar=True)
