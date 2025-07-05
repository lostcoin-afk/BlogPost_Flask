from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from flaskBlogs.services.post_service import create_post, delete_post
from flaskBlogs.models import Post

post_bp = Blueprint('post', __name__)

@post_bp.route('/post/<int:post_id>')
def post(post_id):
    # Fetch the post by ID from the database
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title='Post Page', post=post, hide_sidebar=True)

@post_bp.route('/add_post', methods=['GET', 'POST'])
@login_required
def add_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        is_public = True if request.form.get('is_public') else False
        if title and content:
            create_post(title, content, is_public, current_user)
            flash('Post created successfully!', 'success')
            return redirect(url_for('user.account'))
    return render_template('add_post.html', title='Add Post', hide_sidebar=True)

@post_bp.route('/delete_post/<int:post_id>', methods=['POST'])
@login_required
def delete_post_route(post_id):
    if delete_post(post_id, current_user):
        flash('Post deleted successfully.', 'success')
    else:
        flash('You are not authorized to delete this post.', 'danger')
    return redirect(url_for('user.account'))
