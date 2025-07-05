from flaskBlogs import app, db
from flaskBlogs.forms import RegistrationForm, LoginForm
from flask import render_template, redirect, url_for, flash, request
from flaskBlogs.models import User, Post, Comment
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, login_required, logout_user

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
    posts = Post.query.filter_by(is_public = True).order_by(Post.date_posted.desc()).all()
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About Page')

@app.route('/post/<int:post_id>')
def post(post_id):
    # Fetch the post by ID from the database
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title='Post Page', post=post, hide_sidebar=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)  # This logs the user in and sets current_user
                flash(f'Login successful for: {user.username}', category='success')
                return redirect(url_for('account'))  # No need to pass user/posts here
            else:
                flash('Login Unsuccessful. Please check your email and password.', category='danger')
    return render_template('login.html', title='Login Page', form=form, hide_sidebar=True)

@app.route('/account')
@login_required
def account():
    user = current_user
    posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).all()
    return render_template('user.html', title='Account Page', user=user, posts=posts, hide_sidebar=True)

@app.route('/add_post', methods=['GET', 'POST'])
@login_required
def add_post():
    title = request.form.get('title')
    content = request.form.get('content')
    is_public = True if request.form.get('is_public') else False
    if(title and content):
        post = Post(title=title,content=content,author=current_user,is_public=is_public)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', category='success')
        return redirect(url_for('account'))
    return render_template('add_post.html', title='Add Post', hide_sidebar=True)

@app.route('/delete_post/<int:post_id>', methods=['POST','GET'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash('You are not authorized to delete this post.', 'danger')
        return redirect(url_for('account'))
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('account'))


@app.route('/logout')
@login_required
def logout():
    logout_user()  # This clears the session and logs the user out
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

    # @@@@@@@@@@@@@@@@@@@@----------Concepts on Flask-WTF Forms------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #Registration Form is an instance of Flask Form Class it automatically handles the CSRF token and form validation
    #It automatically populates the form fields with the data submitted by the user even it looks like you are doing a fresh instantiation of the form
    #
    #--------- Check this out --------->  form = RegistrationForm(request.form if request.method == 'POST' else None) 
    #
    # This is because Flask-WTF handles the form data and CSRF(check {{ form.hidden_tag() }} in the register.html and login.html it contains the CSRF token for security purposes) token automatically.
    #So, you don't need to pass the form data explicitly to the template.
    #The form data is automatically available in the form object.

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
            db.session.add(User(name=form.name.data ,username=form.username.data, email=form.email.data, password=hashed_password))
            db.session.commit()

            flash('Registration successful for: ' + form.username.data, category='success') 
            # Here you would typically save the user's information to the database
            # For now, we just redirect to the home page
            print("Registration successful for:", form.username.data)
            return redirect(url_for('login'))
    return render_template('register.html', title='Register Page', form=form, hide_sidebar=True)
