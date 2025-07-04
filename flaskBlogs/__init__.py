from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hg67ih78evds7ubg57iubg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

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

