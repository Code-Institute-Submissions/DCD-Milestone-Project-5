# imports
import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# creating flask instance
app = Flask(__name__)

# Local environement variables, for security.
ROOT_USER = os.environ.get('DB_USERNAME')
ROOT_PASS = os.environ.get('DB_PASSWORD')

app.config["MONGO_URI"] = 'mongodb+srv://{}:{}@recipeclusteralpha.k8y4a.mongodb.net/recipe-site-system?retryWrites=true&w=majority'.format(ROOT_USER, ROOT_PASS)

# pyMongo Constructor
mongo = PyMongo(app)

# app routes

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)  # remove debug for release version
