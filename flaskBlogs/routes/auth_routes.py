# from flaskBlogs import db
# from flaskBlogs.models import Post

# def create_post(title, content, is_public, author):
#     post = Post(title=title, content=content, is_public=is_public, author=author)
#     db.session.add(post)
#     db.session.commit()
#     return post

# def delete_post(post_id, current_user):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         return False
#     db.session.delete(post)
#     db.session.commit()
#     return True

# from flask import Blueprint, request, redirect, url_for, flash, render_template
# from flask_login import login_required, current_user
# from flaskBlogs.services.post_service import create_post, delete_post
# from flaskBlogs.models import Post

# post_bp = Blueprint('post', __name__)

# @post_bp.route('/add_post', methods=['GET', 'POST'])
# @login_required
# def add_post():
#     if request.method == 'POST':
#         title = request.form.get('title')
#         content = request.form.get('content')
#         is_public = True if request.form.get('is_public') else False
#         if title and content:
#             create_post(title, content, is_public, current_user)
#             flash('Post created successfully!', 'success')
#             return redirect(url_for('user.account'))
#     return render_template('add_post.html', title='Add Post', hide_sidebar=True)

# @post_bp.route('/delete_post/<int:post_id>', methods=['POST'])
# @login_required
# def delete_post_route(post_id):
#     if delete_post(post_id, current_user):
#         flash('Post deleted successfully.', 'success')
#     else:
#         flash('You are not authorized to delete this post.', 'danger')
#     return redirect(url_for('user.account'))


# from flaskBlogs.routes.auth_routes import auth_bp
# from flaskBlogs.routes.post_routes import post_bp
# from flaskBlogs.routes.user_routes import user_bp

# app.register_blueprint(auth_bp)
# app.register_blueprint(post_bp)
# app.register_blueprint(user_bp)
from flask import Blueprint, render_template, redirect, url_for, flash
from flaskBlogs.forms import RegistrationForm, LoginForm
from flaskBlogs.services.auth_service import register_user, loginUser
from flask_login import logout_user
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            register_user(form)  # delegate to service layer
            flash(f'Registration successful for: {form.username.data}', 'success')
            return redirect(url_for('auth.login'))
        except ValueError as e:
            flash(str(e), 'danger')
    return render_template('register.html', form=form, title='Register Page', hide_sidebar=True)

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = loginUser(form)
        if user:
            flash(f'Login successful for: {user.username}', 'success')
            return redirect(url_for('user.account'))
        else:
            flash('Login Unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', form=form, title='Login Page', hide_sidebar=True)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))  # Redirect to login page after logout

@auth_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    # Placeholder for forgot password logic
    flash('Forgot password functionality is not implemented yet.', 'info')
    return redirect(url_for('auth.login'))