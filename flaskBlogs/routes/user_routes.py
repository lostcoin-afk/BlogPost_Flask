from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flaskBlogs.services.user_service import get_user_posts, get_all_public_posts

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def home():
    posts = get_all_public_posts()
    return render_template('home.html', title='Home Page', posts=posts, hide_sidebar=True)

@user_bp.route('/about')
def about():
    return render_template('about.html', title='About Page')


@user_bp.route('/account')
@login_required
def account():
    user = current_user
    posts = get_user_posts(user)
    return render_template('user.html', title='Account Page', user=user, posts=posts, hide_sidebar=True)