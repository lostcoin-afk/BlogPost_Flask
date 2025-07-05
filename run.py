from flaskBlogs import create_app, db
import os

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db_path = os.path.join(app.instance_path, 'site.db')
        if os.path.exists(db_path):
            print("Initializing database...")
            db.create_all()
            print("Database initialized successfully.")
        else:
            db.create_all()
            print("Database created successfully.")
    app.run(debug=True)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Implement after Database is ready@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @app.route('/post/<int:post_id>')
# def post(post_id):
#     post = next((p for p in posts if p['id'] == post_id), None)
#     return render_template('post.html', post=post)