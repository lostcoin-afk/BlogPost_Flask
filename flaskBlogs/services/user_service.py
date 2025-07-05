from flaskBlogs.models import Post

def get_all_public_posts():
    return Post.query.filter_by(is_public=True).order_by(Post.date_posted.desc()).all()
def get_user_posts(user):
    return Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).all()