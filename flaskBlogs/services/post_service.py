from flaskBlogs import db
from flaskBlogs.models import Post

def create_post(title, content, is_public, author):
    post = Post(title=title, content=content, is_public=is_public, author=author)
    db.session.add(post)
    db.session.commit()
    return post

def delete_post(post_id, current_user):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        return False
    db.session.delete(post)
    db.session.commit()
    return True
