from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hg67ih78evds7ubg57iubg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskBlogs.models import User


login_manager = LoginManager(app)
login_manager.login_view = 'account'
  # Redirects to 'login' route if not logged in
login_manager.login_message_category = 'info'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



####@@@@@@@@@@@@@@@@@@@@@@________________-------->>>>  NOTES <<<<________________________@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####
#
# this below line is used to import the routes after the app and db are initialized to avoid circular import and a race condition.
# The below import of routes might look unnecessary, but it is essential to ensure that the routes are registered after the app and db are initialized.
# Because the Flask app doesnt scan the routes.py file until it is imported, as a result the routes are not registered and hence you will get a 404 URL not found error whenever you try to access the routes. 
# 
# 
# If you place the import at the top, it will cause a circular import error because routes.py tries to import app and db from this module, and this module tries to import routes.py.
# This is a common pattern in Flask applications to avoid circular imports.

from flaskBlogs import routes

