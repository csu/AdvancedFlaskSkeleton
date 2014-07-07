#!/usr/bin/env python
import os
from flask import Flask, render_template, jsonify, request
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

#####################################################################
# Check if running locally on on Heroku and setup MongoDB accordingly
#####################################################################
app.config["MONGODB_SETTINGS"] = {
    'DB': 'my_app'
}
app.config["SECRET_KEY"] = "asdjhfa87sdfas78df"  # used for csrf forms

on_heroku = False
if 'MONGOLAB_URI' in os.environ:
  on_heroku = True

if on_heroku:
    app.config["MONGODB_SETTINGS"]["host"] = os.environ['MONGOLAB_URI']
else:
    app.config["MONGODB_SETTINGS"]["host"] = 'mongodb://localhost:27017/'  # not necessary

db = MongoEngine(app)

#####################################################################
# Models
#####################################################################
from models.post_model import *

#####################################################################
# Views
#####################################################################
def register_blueprints(app):
    # Prevents circular imports
    from views.views import posts
    app.register_blueprint(posts)

register_blueprints(app)

#####################################################################
# Start Flask
#####################################################################

if __name__ == '__main__':
    app.run(debug=True)