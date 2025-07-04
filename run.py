from flaskBlogs import app, db

import os
if( __name__ == '__main__'):
    with app.app_context():
        if os.path.exists('instance/site.db'):
            print("Initializing database...")
            db.create_all()
            print("Database initialized successfully.")
        else:
            db.create_all()
            print("Database Created Successfully.")
    app.run(debug=True)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Implement after Database is ready@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @app.route('/post/<int:post_id>')
# def post(post_id):
#     post = next((p for p in posts if p['id'] == post_id), None)
#     return render_template('post.html', post=post)