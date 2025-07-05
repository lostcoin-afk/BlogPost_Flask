from flaskBlogs import db
from flaskBlogs.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

def register_user(form):
    if User.query.filter_by(email=form.email.data).first():
        raise ValueError("Email already registered.")
    if User.query.filter_by(username=form.username.data).first():
        raise ValueError("Username already taken.")

    hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
    user = User(
        name=form.name.data,
        username=form.username.data,
        email=form.email.data,
        password=hashed_password
    )
    db.session.add(user)
    db.session.commit()
    return user

def loginUser(form):
    user = User.query.filter_by(email=form.email.data).first()
    if user and check_password_hash(user.password, form.password.data):
        login_user(user)
        return user
    return None

def logout_user():
    # Flask-Login handles the logout process, so this function can be empty
    pass
