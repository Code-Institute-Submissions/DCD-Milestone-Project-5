# imports
import os
from flask import Flask, render_template, redirect, request, url_for
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
    return render_template("home.html", recipes_popular=mongo.db.recipes.find(), recipes_new=mongo.db.recipes.find())


@app.route('/recipes')
def recipe_search():
    return render_template("recipe_list.html", recipes=mongo.db.recipes.find())


@app.route('/recipes/<ID>')
def recipe_page(ID):
    return render_template("recipe_page.html")


@app.route('/edit_recipe')
def edit_recipe():
    return render_template("edit_recipe.html")


@app.route('/insert_recipe', methods=["GET", "POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('recipe_search'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)  # remove debug for release version
