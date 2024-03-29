# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    print(error)
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable
from app.modulehelloworld.controller.hello_world import simple_page

# Register blueprint(s)
app.register_blueprint(simple_page)

# Build the database:
# This will create the database file using SQLAlchemy
db.drop_all()
db.create_all()
from app.modulehelloworld.service import hello_world
hello_world.create_test_user()